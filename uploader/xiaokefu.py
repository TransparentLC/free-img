import random
import string

from uploader import AbstractUploader
from urllib.parse import unquote

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://xiaokefu.com.cn/pcAccess/H5UploadImage'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def form(self) -> dict:
        return {
            'token': 'd2c284db92c9b3aaf844ed38da395962',
            'id': 8,
        }

    @property
    def parsed(self) -> str:
        return self.request.json()['data'][0]['image_url']
