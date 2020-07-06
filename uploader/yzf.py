import json
import random

from _abstract import AbstractUploader
from urllib.parse import unquote

class YzfUploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://yzf.qq.com/fsnb/kf-file/upload_wx_media'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def form(self) -> dict:
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        userid = list(map(lambda x: random.choice(chars), range(18)))
        userid[15] += '_'
        userid = f'kf{"".join(userid)}'
        return {
            'mid': 'fsnb',
            'media_type': 'image',
            'userid': userid
        }

    @property
    def parsed(self) -> str:
        return unquote(json.loads(self.request.text)['KfPicUrl']).split('?')[0]
