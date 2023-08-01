**MinneApple: A benchmark dataset for apple detection and segmentation** is a dataset for instance segmentation, object detection, and semantic segmentation tasks. It is used in the agricultural industry. 

The dataset consists of 1001 images with 23065 labeled objects belonging to 1 single class (*apple*).

Images in the MinneApple dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 331 (33% of the total) unlabeled images (i.e. without annotations). There are 2 splits in the dataset: *Test* (331 images) and *Train* (670 images). The dataset was released in 2019 by the University of Minnesota Robotic Sensor Network Laboratory.

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/minne-apple/raw/main/visualizations/side_annotations_grid.png">
