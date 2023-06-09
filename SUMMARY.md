**MinneApple** (MinneApple: A Benchmark Dataset for Apple Detection and Segmentation) is a dataset for semantic segmentation, object detection, and instance segmentation tasks. It is used in the agriculture industry.

The dataset consists of 1001 images with 23065 labeled objects belonging to 1 single class (*apple*).

Each image in the MinneApple dataset has pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 331 (33% of the total) unlabeled images (i.e. without annotations). There are 2 splits in the dataset: *Test* (331 images) and *Train* (670 images). The dataset was released in 2019 by the [University of Minnesota Robotic Sensor Network Laboratory](https://rsn.umn.edu/).

Here is the visualized grid with sample images and masks:

<img src="https://github.com/dataset-ninja/minne-apple/raw/main/visualizations/side_annotations_grid.png">
