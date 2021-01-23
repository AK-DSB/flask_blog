from flask import Flask
from apps.users import views as user_view
from apps.articles import views as article_view
from apps.goods import views as goods_view
from extends import db, bootstrap, cache
import settings

# 配置任redis缓存
config = {
    'CACHE_TYPE': 'redis',  # 缓存类型数据库
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_PORT': 6379
}


def create_app():

    app = Flask(__name__, template_folder='../templates', static_folder='../static', static_url_path='/')
    app.config.from_object(settings.Production)
    app.register_blueprint(blueprint=user_view.user_bp)
    app.register_blueprint(blueprint=article_view.article_bp, url_prefix='/article')
    app.register_blueprint(blueprint=goods_view.goods_bp, url_prefix='/goods')
    # 初始化db
    db.init_app(app=app)

    # 初始化bootstrap
    bootstrap.init_app(app=app)
    # 初始化缓存文件
    cache.init_app(app=app, config=config)
    return app
