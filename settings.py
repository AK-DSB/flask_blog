import os


class BaseConfig(object):
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = '@#$%^&*'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:FW249746@127.0.0.1:3306/flask_blog?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # 项目路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
    UPLOAD_ICON_DIR = os.path.join(BASE_DIR, 'static/upload/icon')
    # 相册
    UPLOAD_PHOTO_DIR = os.path.join(BASE_DIR, 'static/upload/photo')


class Production(BaseConfig):
    ENV = 'production'


if __name__ == '__main__':
    print(BaseConfig.UPLOAD_ICON_DIR)