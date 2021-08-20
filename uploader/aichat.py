import os

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://upload.aichat.net/upload/single'

    @property
    def file_key(self) -> str:
        return 'single'

    @property
    def parsed(self) -> str:
        return self.request.json()['url']

    def filename_rewrite(self, filename: str) -> str:
        if os.path.splitext(filename.lower())[1] not in {'.jpg', '.jpeg', '.gif', '.png', '.webp'}:
            filename += '.jpg'
        return filename
