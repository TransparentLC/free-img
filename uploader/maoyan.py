import json
import os

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://maoyan.com/ajax/proxy/admin/mmdb/photos/upload.json'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['data'][0]['olink'].replace('http://', 'https://')

    def filename_rewrite(self, filename: str) -> str:
        if os.path.splitext(filename.lower())[1] in ('.webp', '.avif'):
            filename += '.jpg'
        return filename
