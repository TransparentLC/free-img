import json

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://baijiahao.baidu.com/builderinner/api/content/file/upload'

    @property
    def file_key(self) -> str:
        return 'media'

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['ret']['https_url']
