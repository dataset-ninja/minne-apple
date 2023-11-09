import os
import random
import tarfile
from typing import Literal

import gdown
import pandas as pd
import supervisely as sly
import tqdm
from cv2 import connectedComponents
from supervisely.io.fs import get_file_name, get_file_name_with_ext, get_file_size

import src.sly_globals as g


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # if not os.path.exists(archive_path):
    #     gdown.download(apple_url, archive_path, quiet=False)
    # extract_tar()

    work_dir_path = "/home/grokhi/rawdata/minne-apple"
    datasets = [
        "counting-train",
        "counting-val",
        "counting-test",
        "detection-train",
        "detection-test",
    ]

    images_folder = "images"
    anns_folder = "masks"
    batch_size = 100

    def create_ann(image_path):
        labels, tags = [], []
        import cv2

        image_np = sly.imaging.image.read(image_path)[:, :, :]
        image_np = image_np[:, :, 0]

        if task == "detection":
            ann_path = os.path.join(curr_ann_path, get_file_name_with_ext(image_path))
            ann_np = sly.imaging.image.read(ann_path)
            ann_np_gray = cv2.cvtColor(ann_np, cv2.COLOR_BGR2GRAY)

            ann_bool = ann_np_gray != 0

            ret, curr_mask = connectedComponents(ann_bool.astype("uint8"), connectivity=8)
            for i in range(1, ret):
                obj_mask = curr_mask == i
                bitmap = sly.Bitmap(obj_mask)
                label = sly.Label(bitmap, apple_class)
                labels.append(label)

            return sly.Annotation(img_size=(image_np.shape[0], image_np.shape[1]), labels=labels)

        elif task == "counting":
            file_path = os.path.join(apple_data_path, f"{split}_ground_truth.txt")

            df = pd.read_csv(file_path)
            filtered_df = df[df["Image"] == get_file_name_with_ext(image_path)]

            # If the filtered DataFrame is not empty, print the 'count' value
            if not filtered_df.empty:
                val = int(filtered_df["count"].values[0])
                tags = [
                    sly.Tag(tag_meta, value=val)
                    for tag_meta in tag_metas
                    if tag_meta.name == count_tag.name
                ]
            else:
                print("No entry found for the given image name:", image_path)

            return sly.Annotation(img_size=(image_np.shape[0], image_np.shape[1]), img_tags=tags)

    count_tag = sly.TagMeta("count", sly.TagValueType.ANY_NUMBER)
    apple_class = sly.ObjClass("apple", sly.Bitmap)

    new_project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    tag_metas = [count_tag]
    meta = sly.ProjectMeta(obj_classes=[apple_class], tag_metas=tag_metas)
    api.project.update_meta(new_project.id, meta.to_json())

    for ds_name in datasets:
        task, split = ds_name.split("-")
        apple_data_path = os.path.join(work_dir_path, task, split)

        new_dataset = api.dataset.create(new_project.id, ds_name, change_name_if_conflict=True)

        curr_img_path = os.path.join(apple_data_path, images_folder)
        curr_ann_path = os.path.join(apple_data_path, anns_folder)

        img_ext = ".jpg" if ds_name == "counting-test" else ".png"

        img_names = [name for name in os.listdir(curr_img_path) if name.endswith(img_ext)]

        with tqdm.tqdm(
            desc="Create dataset {}".format(ds_name), total=count_files(curr_img_path, img_ext)
        ) as pbar:
            for img_names_batch in sly.batched(img_names, batch_size=batch_size):
                img_pathes = [os.path.join(curr_img_path, name) for name in img_names_batch]
                img_infos = api.image.upload_paths(new_dataset.id, img_names_batch, img_pathes)
                img_ids = [im_info.id for im_info in img_infos]

                if split in ["train", "val"]:
                    anns = [create_ann(img_path) for img_path in img_pathes]
                    api.annotation.upload_anns(img_ids, anns)

                pbar.update(len(img_names_batch))

    return new_project
