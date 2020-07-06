import json

from _abstract import AbstractUploader

class YidianzixunUploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://mp.yidianzixun.com/upload?action=uploadimage'

    @property
    def file_key(self) -> str:
        return 'upfile'

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['url']
