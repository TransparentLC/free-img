import json
import os

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://kfupload.alibaba.com/mupload'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def form(self) -> dict:
        ext = os.path.splitext(self.path)[1]
        if ext.lower() not in ['.jpg', '.jpeg', '.gif', '.png']:
            ext = '.jpg'
        return {
            'scene': 'productImageRule',
            'name': f'image{ext}'
        }

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['url']
