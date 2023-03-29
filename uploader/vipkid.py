import os

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://www.vipkid.com/rest/gw/api/upload/vos'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def form(self) -> dict:
        return {
            'uploadType': 'IM',
        }

    @property
    def headers(self) -> dict:
        return {
            'vk-cr-code': 'kr',
        }

    def filename_rewrite(self, filename: str) -> str:
        if os.path.splitext(filename.lower())[1] in {'.webp', '.avif'}:
            filename += '.jpg'
        return filename

    @property
    def parsed(self) -> str:
        return self.request.json()['data']['url']