**MinneApple: A Benchmark Dataset for Apple Detection and Segmentation** is a dataset for instance segmentation, semantic segmentation, object detection, and counting tasks. It is used in the agricultural industry. 

The dataset consists of 69982 images with 23065 labeled objects belonging to 1 single class (*apple*).

Images in the MinneApple dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 69312 (99% of the total) unlabeled images (i.e. without annotations). There are 5 splits in the dataset: *counting-train* (64595 images), *counting-val* (3395 images), *counting-test* (991 images), *detection-train* (670 images), and *detection-test* (331 images). The dataset was released in 2019 by the <span style="font-weight: 600; color: grey; border-bottom: 1px dashed #d3d3d3;">University of Minnesota Robotic Sensor Network Laboratory</span>.

Here is the visualized example grid with animated annotations:

[animated grid](https://github.com/dataset-ninja/minne-apple/raw/main/visualizations/horizontal_grid.webm)
