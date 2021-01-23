import datetime

from extends import db


class ArticleType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(20), nullable=False)
    articles = db.relationship('Article', backref='type')

    __table_rgs = {
        'extend_existing': True,
        'mysql_charset': 'utf-8'
    }

    def __str__(self):
        return self.type_name


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.BLOB, nullable=False)
    publish_date = db.Column(db.DateTime, default=datetime.datetime.now)
    click_num = db.Column(db.Integer, default=0)
    save_num = db.Column(db.Integer, default=0)
    love_num = db.Column(db.Integer, default=0)
    # 建立外键关系
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('article_type.id'), nullable=False)
    comments = db.relationship('Comment', backref='article')

    __table_args = {
        'extend_existing': True,
        'mysql_charset': 'utf-8'
    }

    def __str__(self):
        return self.title


class Comment(db.Model):
    # 自定义表名
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    comment_date = db.Column(db.DateTime, default=datetime.datetime.now)

    __table_args = {
        'extend_existing': True,
        'mysql_charset': 'utf8'
    }

    def __str__(self):
        return self.comment
