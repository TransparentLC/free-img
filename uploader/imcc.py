import re

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://uccfile.im-cc.com/upload/'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def parsed(self) -> str:
        return 'https://uccfile.im-cc.com/download/' + re.search(r'<url>(.*?)</url>', self.request.text).group(1)
