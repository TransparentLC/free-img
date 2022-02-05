from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://help.baidu.com/api/mpic'

    @property
    def file_key(self) -> str:
        return 'pic'

    @property
    def parsed(self) -> str:
        return self.request.json()['resps'][0]
