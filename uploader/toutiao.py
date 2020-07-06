import json

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://mp.toutiao.com/upload_photo/?type=json'

    @property
    def file_key(self) -> str:
        return 'photo'

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['web_url']
