import random

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://myjd.jd.com/afs/common/upload.action'

    @property
    def file_key(self) -> str:
        return 'filedata'

    @property
    def form(self) -> dict:
        return {
            'op': 'applyUpload',
        }

    @property
    def parsed(self) -> str:
        return f'https://img{random.choice((1, *range(10, 15), 20, 30))}.360buyimg.com/myjd/{self.request.json()["optDescription"]}'
