import json

from _abstract import AbstractUploader

class GtimgUploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://om.qq.com/image/orginalupload'

    @property
    def file_key(self) -> str:
        return 'Filedata'

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['data']['url'].replace('http://', 'https://')


print(GtimgUploader(r"C:\Users\Admin\Desktop\J9qzRJx_2.jpg").upload())
