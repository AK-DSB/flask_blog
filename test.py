# # -*- coding: utf-8 -*-
# # flake8: noqa
#
# from qiniu import Auth, put_file, etag
# import qiniu.config
# import os
#
# #需要填写你的 Access Key 和 Secret Key
# from flask_blog.settings import BaseConfig
#
# access_key = 'TR4lEDU4BWm9Y3ZQLTJAXeumnAxASYHz-Ba6X9ah'
# secret_key = 'W9gfOpkZeskwAJtmPnMxd1zN4wDf7u5_cRxpkyeW'
#
# #构建鉴权对象
# q = Auth(access_key, secret_key)
#
# #要上传的空间
# bucket_name = 'akwblog'
#
# #上传后保存的文件名
# key = 'my-python-logo.png'
#
# #生成上传 Token，可以指定过期时间等
# token = q.upload_token(bucket_name, key, 3600)
#
# #要上传文件的本地路径
# localfile = os.path.join(BaseConfig.UPLOAD_ICON_DIR, 'Erha.jpg')
#
# ret, info = put_file(token, key, localfile)
# # print(info)
# # assert ret['key'] == key
# # assert ret['hash'] == etag(localfile)
# print(ret)
# print(info)
#
# '''
# {'hash': 'Flk3FGaG7VFVYHhO0DcSaOhvirzn', 'key': 'my-python-logo.png'}
# _ResponseInfo__response:<Response [200]>, exception:None, status_code:200,
# text_body:{"hash":"Flk3FGaG7VFVYHhO0DcSaOhvirzn","key":"my-python-logo.png"}, req_id:r04AAABnalsfI1kW, x_log:X-Log
# '''

# -*- coding: utf-8 -*-
# flake8: noqa
# from qiniu import Auth
# from qiniu import BucketManager
# access_key = 'TR4lEDU4BWm9Y3ZQLTJAXeumnAxASYHz-Ba6X9ah'
# secret_key = 'W9gfOpkZeskwAJtmPnMxd1zN4wDf7u5_cRxpkyeW'
# #初始化Auth状态
# q = Auth(access_key, secret_key)
# #初始化BucketManager
# bucket = BucketManager(q)
# #你要测试的空间， 并且这个key在你空间中存在
# bucket_name = 'akwblog'
# key = '3.jpg'
# #获取文件的状态信息
# ret, info = bucket.stat(bucket_name, key)
# print(info)

# dic = {'a': 1, 'b': 2}
# dic.update(a=2)
# print(dic)