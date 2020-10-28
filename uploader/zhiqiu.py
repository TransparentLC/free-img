import json

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://zhiqiu.baidu.com/imcswebchat/api/file/upload'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def headers(self) -> dict:
        return {
            'Referer': 'https://zhiqiu.baidu.com/imcswebchat/plugin/',
        }

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['url']
