
from apps import create_app
from flask_script import Manager
from extends import db
from flask_migrate import Migrate, MigrateCommand
from apps.users.models import User, Photo  # 必须导入，执行migrate时才会检索到这些表
from apps.articles.models import Article, ArticleType


app = create_app()
manager = Manager(app=app)
migrate = Migrate(app=app, db=db)
manager.add_command('makemigrations', MigrateCommand)


@manager.command
def init():
    print('初始化')


if __name__ == '__main__':
    # print(app.url_map)
    manager.run()