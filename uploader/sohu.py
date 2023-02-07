import json

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://changyan.sohu.com/api/2/comment/attachment'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def form(self) -> dict:
        return {
            'type': 'feedback',
        }

    @property
    def parsed(self) -> str:
        return json.loads(self.request.json())['url']