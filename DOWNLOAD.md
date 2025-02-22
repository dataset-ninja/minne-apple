Dataset **MinneApple** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzI5MjVfTWlubmVBcHBsZS9taW5uZWFwcGxlLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIllZVDRjMjNBaVZ5Mnh5RWxmcm9zVFQzVUppVjZ2U2JQbnZFVUJPeVgxNFE9In0=)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='MinneApple', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [Description of data](https://conservancy.umn.edu/bitstream/handle/11299/206575/MinneApple%20Data%20README.txt?sequence=14&isAllowed=y)
- [Patch-based fruit counting dataset (2,875 JPG files and 67,990 PNG files)](https://conservancy.umn.edu/bitstream/handle/11299/206575/counting.tar.gz?sequence=1&isAllowed=y)
- [Fruit detection and segmentation dataset (1,671 PNG files)](https://conservancy.umn.edu/bitstream/handle/11299/206575/detection.tar.gz?sequence=2&isAllowed=y)
- [Test data with test labels for counting, detection, and segmentation](https://conservancy.umn.edu/bitstream/handle/11299/206575/test_data.zip?sequence=16&isAllowed=y)
