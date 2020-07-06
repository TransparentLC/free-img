import json

from _abstract import AbstractUploader

class ChangyanUploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://changyan.sohu.com/api/2/comment/attachment'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text[1:-1].replace('\\\"','"'))['url']
