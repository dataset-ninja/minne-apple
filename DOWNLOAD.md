Dataset **MinneApple** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/j/0/Vz/daImiEimWtbLk0WvuklRpaYnvByyXROEbeFH0DWvXj05NYRH2NTPXB0xyiNQp9b03GmcXBmTPp59PeCe5whghBwRvD4MkmIxOZewwLsrAsEbMY08NEhCFU4fNmlh.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='MinneApple', dst_path='~/dtools/datasets/MinneApple.tar')
```
The data in original format can be downloaded here:

- 🔗[Description of data](https://conservancy.umn.edu/bitstream/handle/11299/206575/MinneApple%20Data%20README.txt?sequence=14&isAllowed=y)
- 🔗[Patch-based fruit counting dataset (2,875 JPG files and 67,990 PNG files)](https://conservancy.umn.edu/bitstream/handle/11299/206575/counting.tar.gz?sequence=1&isAllowed=y)
- 🔗[Fruit detection and segmentation dataset (1,671 PNG files)](https://conservancy.umn.edu/bitstream/handle/11299/206575/detection.tar.gz?sequence=2&isAllowed=y)
- 🔗[Test data with test labels for counting, detection, and segmentation](https://conservancy.umn.edu/bitstream/handle/11299/206575/test_data.zip?sequence=16&isAllowed=y)
