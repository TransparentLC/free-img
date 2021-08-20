import random
import string

from uploader import AbstractUploader
from urllib.parse import unquote

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://yzf.qq.com/fsnb/kf-file/upload_wx_media'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def form(self) -> dict:
        userid = list(map(lambda x: random.choice(string.ascii_letters + string.digits), range(18)))
        userid[15] += '_'
        userid = f'kf{"".join(userid)}'
        return {
            'mid': 'fsnb',
            'media_type': 'image',
            'userid': userid
        }

    @property
    def parsed(self) -> str:
        return unquote(self.request.json()['KfPicUrl']).split('?')[0]
