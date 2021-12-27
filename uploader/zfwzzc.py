import base64

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return base64.b85decode(b'XmoUNb2=|CdS-WedSfnkcXuvlZ+0$YZZBhKWn*h!cV%KPb#QENVPs!sX>4UxaBOd3WG-Q2bZKvHKV)fgJ!x%WXJr').decode()

    @property
    def file_key(self) -> str:
        return 'imgFile'

    @property
    def parsed(self) -> str:
        return base64.b85decode(b'XmoUNb2=|CdS-WedSfnkcXuvlZ+0$YZU').decode() + self.request.json()['url']
