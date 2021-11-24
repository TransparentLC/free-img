# free-img

一个自用的图片上传工具。

*仅供学习交流使用，不保证上传后的 URL 的有效性。*

```console
[root@localhost free-img]# cli/free-img.py -i image.jpg -s alicdn
image.jpg -> https://ae01.alicdn.com/kf/Ue6091d8f8ab344e0b2f6726d22e2d6c9x.jpg
[root@localhost free-img]# cli/free-img.py -i image.jpg -s toutiao -f markdown
image.jpg -> ![image.jpg](https://p.pstatp.com/origin/fe960003179ab14c66f8)
[root@localhost free-img]# cli/free-img.py -i image.jpg -s zhidao -f html -r
<img alt="image.jpg" src="https://iknow-pic.cdn.bcebos.com/060828381f30e9242a16d04c5c086e061d95f719">
```

## 命令行参数

| 参数 | 简写 | 作用 |
| --- | --- | --- |
| `--input` | `-i` | 需要上传的图片路径，可以输入多个，必须填写 |
| `--server` | `-s` | 上传的图床，参见下面的“支持的图床”，必须填写 |
| `--format` | `-f` | 上传后输出 URL 的格式，默认为 `plain` 输出原始 URL，也可以选择 `markdown`、`html`、`bbcode` 这几种格式 |
| `--raw` | `-r` | 直接在标准输出中显示 URL，不显示文件名 |
| `--glob` | `-g` | 使用 glob 的规则解析图片路径，这样就可以使用 `*` 之类的通配符了 |
| `--help` | `-h` | 显示帮助 |

## 支持的图床

<details>
<summary>展开内容</summary>

| 名称 | 上传后的 URL |
| --- | --- |
| 7moor <sup>\*</sup> <sup>\*\*</sup> | [fs-im-kefu.7moor-fs2.com](https://fs-im-kefu.7moor-fs2.com/im/2768a390-5474-11ea-afc9-7b323e3e16c0/f-_gRKJY3BBbXnlp.jpg) |
| aichat <sup>\*</sup> <sup>\*\*</sup> | [static.aichat.net](https://static.aichat.net/chat/202108/205d94f2-40e0-49db-b738-75e5d9d68653.jpg) |
| alicdn <sup>\*</sup> <sup>\*\*</sup> | [ae01.alicdn.com](https://ae01.alicdn.com/kf/Ue6091d8f8ab344e0b2f6726d22e2d6c9x.jpg) |
| baijiahao | [pic.rmb.bdstatic.com](https://pic.rmb.bdstatic.com/bjh/32d650f5ac7d08cb701789e98c5bdead.jpeg) |
| baike | [bkimg.cdn.bcebos.com](https://bkimg.cdn.bcebos.com/pic/b3119313b07eca806538c935186a80dda144ac342585) |
| dianping <sup>\*</sup> <sup>\*\*</sup> | [p0.meituan.net](https://p0.meituan.net/csc/32d650f5ac7d08cb701789e98c5bdead65846.jpg) |
| dingyue | [dingyue.ws.126.net](https://dingyue.ws.126.net/2020/1028/32d650f5j00qiw1ok001sd000go00gop.jpg) |
| gtimg | [inews.gtimg.com](https://inews.gtimg.com/newsapp_ls/0/12067385341/0) |
| imgurl <sup>\*</sup> | [ftp.bmp.ovh](https://ftp.bmp.ovh/imgs/2020/07/ac7d08cb701789e9.jpg) |
| jd | [img*.360buyimg.com](https://img20.360buyimg.com/myjd/jfs/t1/128109/13/6838/65846/5f086444E1dc00680/b977b3bace25c778.jpg) |
| ldmnq <sup>\*</sup> <sup>\*\*</sup> | [ldbbs.ldmnq.com](https://ldbbs.ldmnq.com/bbs/topic/attachment/2021-7/9287ebd6-df0b-428e-8a6f-703f328d3482.jpg) |
| maoyan <sup>\*</sup> <sup>\*\*</sup> | [p0.meituan.net](https://p0.meituan.net/mmdb/32d650f5ac7d08cb701789e98c5bdead65846.jpg) |
| oppo | [cdofs.oppomobile.com](https://cdofs.oppomobile.com/cdo-portal/feedback/202107/16/9715e4b42dfc721dfa437bf597b834ce.jpg) |
| uploadcc | [upload.cc](https://upload.cc/i1/2020/07/25/p5TNES.jpg) |
| wenku | [wkphoto.cdn.bcebos.com](https://wkphoto.cdn.bcebos.com/fcfaaf51f3deb48fd81fbabce01f3a292df57859.jpg) |
| yidianzixun <sup>\*</sup> | [si1.go2yd.com](https://si1.go2yd.com/get-image/0iFKu4YVCsK) |
| yunque360 <sup>\*</sup> <sup>\*\*</sup> | [yunque-chat.oss.yunque360.com](https://yunque-chat.oss.yunque360.com/20210913/a1/cb/a1cba508fff22a915b3245d4be249352.jpg) |
| yzf | [yzf.qq.com](https://yzf.qq.com/fsnb/kf-file/kf_pic/20200710/KFPIC_hF_WXIMAGE_MihOPneDLPHDtWHTTCdH.jpg) |
| zhidao | [iknow-pic.cdn.bcebos.com](https://iknow-pic.cdn.bcebos.com/060828381f30e9242a16d04c5c086e061d95f719) |
| ~~httpbin~~ | 仅用于测试 |

> 测试用图片的出处：[Pixiv ID #72467059](https://www.pixiv.net/artworks/72467059)
>
> <sup>\*</sup> 支持 WebP
>
> <sup>\*\*</sup> 支持 AVIF
>
> 部分图床还可能存在以下特性：
>
> * 对图片进行二压，可能的条件包括但不限于：图片尺寸/大小超过一定范围、上传后超过一段时间、访问时存在响应头 `Accept: image/webp, ...`、无条件二压……
> * 通过修改扩展名而不修改文件内容，可以上传任意格式的文件
> * 支持 CORS，访问上传后的图片 URL 时可以给出 `Access-Control-Allow-Origin: *` 的响应头

</details>

## 自行添加上传模块

在 `uploader` 目录下新建文件，新建一个类 `Uploader`，继承 [`uploader/__init__.py`](https://github.com/TransparentLC/free-img/blob/master/uploader/__init__.py) 中的 `AbstractUploader`，然后重写其中的属性和方法即可。

<details>
<summary>展开内容</summary>

```python
from uploader import AbstractUploader

class Uploader(AbstractUploader):
    # 用于上传的图床接口 URL
    @property
    @abstractmethod
    def request_url(self) -> str:
        pass

    # 进行上传的表单中，文件对应的key
    @property
    @abstractmethod
    def file_key(self) -> str:
        pass

    # 表单中的其他内容
    # 没有的话就不需要重写
    @property
    def form(self) -> dict:
        pass

    # 从请求的响应中解析图片 URL
    # 可以通过 self.requests 获取发送请求的 requests 对象
    # 不重写的话，默认将直接返回响应内容
    @property
    def parsed(self) -> str:
        pass

    # 自定义请求头
    # 将会合并/覆盖以下默认请求头：
    # { 'User-Agent': （IE11 的 UA）, 'X-Forwarded-For': （随机的 IP 地址） }
    @property
    def headers(self) -> dict:
        pass

    # 在上传时返回重写的文件名
    # 某些图床只检查扩展名而不是从文件内容中检查格式，这时就可以通过重写文件名来绕过检查
    # 例如：在这里将一张 webp 图片的扩展名改为 jpg 并返回，在某些图床即可正常上传
    def filename_rewrite(self, filename: str) -> str:
        pass

    # 返回图片上传后的 URL
    # self.path 为本地的图片文件路径
    # 使用 self.request 保存发送请求的 requests 对象
    # 通过 self.parsed 获取 URL 并返回（当然也可以不使用，直接在这里解析）
    # 除非有特殊需求，这个方法不一定需要重写
    def upload(self) -> str:
        pass
```
</details>

可以参考用于测试的上传模块 [`uploader/httpbin.py`](https://github.com/TransparentLC/free-img/blob/master/uploader/httpbin.py)。