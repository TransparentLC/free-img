import json

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://upload.cc/image_upload'

    @property
    def file_key(self) -> str:
        return 'uploaded_file[]'

    @property
    def parsed(self) -> str:
        return f'https://upload.cc/{json.loads(self.request.text)["success_image"][0]["url"]}'
