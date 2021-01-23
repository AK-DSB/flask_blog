from qiniu import Auth, put_file, etag, put_data, BucketManager
import qiniu.config
import os
from settings import BaseConfig
import random

from apps.users.smssend import SmsSendAPIDemo, SecretPair


def upload_qiniu(filesorage):
    access_key = 'TR4lEDU4BWm9Y3ZQLTJAXeumnAxASYHz-Ba6X9ah'
    secret_key = 'W9gfOpkZeskwAJtmPnMxd1zN4wDf7u5_cRxpkyeW'
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'akwblog2'

    # 上传后保存的文件名
    filename = filesorage.filename
    name = filename.rsplit('.')[0] + '_' + str(random.randint(1, 1000)) + '.' + filename.rsplit('.')[-1]
    key = name

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)

    # 要上传文件的本地路径
    # localfile = os.path.join(BaseConfig.UPLOAD_ICON_DIR, 'Erha.jpg')
    #
    # ret, info = put_file(token, key, localfile)
    ret, info = put_data(token, key, filesorage.read())
    # 返回上传后返回的信息和key，key要存到数据库中
    return ret, info


def delete_qiniu(photo):
    access_key = 'TR4lEDU4BWm9Y3ZQLTJAXeumnAxASYHz-Ba6X9ah'
    secret_key = 'W9gfOpkZeskwAJtmPnMxd1zN4wDf7u5_cRxpkyeW'
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'akwblog2'

    # 初始化Auth状态
    q = Auth(access_key, secret_key)
    # 初始化BucketManager
    bucket = BucketManager(q)
    # 你要测试的空间， 并且这个key在你空间中存在
    key = photo.photo_name
    # 删除bucket_name 中的文件 key
    ret, info = bucket.delete(bucket_name, key)
    print(info)
    return ret, info


def send_messages(phone):
    SECRET_ID = "dcc535cbfaefa2a24c1e6610035b6586"  # 产品密钥ID，产品标识
    SECRET_KEY = "d28f0ec3bf468baa7a16c16c9474889e"  # 产品私有密钥，服务端生成签名信息使用，请严格保管，避免泄露
    BUSINESS_ID = "748c53c3a363412fa963ed3c1b795c65"  # 业务ID，易盾根据产品业务特点分配
    secret_pair = SecretPair(SECRET_ID, SECRET_KEY)
    api = SmsSendAPIDemo(BUSINESS_ID, secret_pair)
    # 产生随机验证码
    code = ""
    for i in range(4):
        ran = random.randint(0, 9)
        code += str(ran)
    params = {
        "mobile": phone,
        "templateId": "10084",
        "paramType": "json",
        "params": {"code": code}
        # 国际短信对应的国际编码(非国际短信接入请注释掉该行代码)
        # "internationalCode": "对应的国家编码"
    }
    ret = api.send(params=params)

    return ret, code