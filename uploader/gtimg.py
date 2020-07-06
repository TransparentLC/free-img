import json

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://om.qq.com/image/orginalupload'

    @property
    def file_key(self) -> str:
        return 'Filedata'

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['data']['url'].replace('http://', 'https://')
