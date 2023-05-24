import os
import secrets

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://www.yingyuchat.com/uploadimg'

    @property
    def file_key(self) -> str:
        return 'imgfile'

    @property
    def form(self) -> dict:
        return {
            'acountname': secrets.token_urlsafe(6),
        }

    def filename_rewrite(self, filename: str) -> str:
        if os.path.splitext(filename.lower())[1] in {'.webp', '.avif'}:
            filename += '.jpg'
        return filename

    @property
    def parsed(self) -> str:
        return self.request.json()['data']['url']