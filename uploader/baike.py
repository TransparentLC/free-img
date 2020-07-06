import json

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://baike.baidu.com/wikisubmit/api/albumupload'

    @property
    def file_key(self) -> str:
        return 'filedata'

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['bigImgUrls'].split('?')[0]
