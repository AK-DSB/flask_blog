import datetime

from extends import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(101), nullable=False)
    phone = db.Column(db.String(11), nullable=False, unique=True)
    email = db.Column(db.String(30))
    icon = db.Column(db.String(100))
    is_delete = db.Column(db.Boolean, default=False)
    register_time = db.Column(db.DateTime, default=datetime.datetime.now)
    # 增加一个字段，不会出现在数据库中,relationship()是在view和template中体现价值的
    #                                      backref:反向引用，通过文章找user
    # lay决定了sqlalchemy什么时候从数据库中加载数据，dynamic在有多条数据的时候特别有用，不是直接加载这些数据
    # 默认是select
    articles = db.relationship('Article', backref='user')
    comments = db.relationship('Comment', backref='user')
    __table_args__ = {
        'extend_existing': True,
        'mysql_charset': 'utf8'
    }

    def __str__(self):
        return self.username


class Photo(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    photo_name = db.Column(db.String(32), nullable=False)
    photo_datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    __table_args = {
        'extend_existing': True,
        'mysql_charset': 'utf-8'
    }

    def __str(self):
        return self.photo_name


class AboutMe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.BLOB, nullable=False)
    pdatetime = db.Column(db.DateTime, default=datetime.datetime.now)
    # 与用户建立联系
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)  # unique没有设置成True，查询出来的话会是一个列表，flask里的外键都是一对多
    user = db.relationship('User', backref='about')

    __table__args = {
        'extend_existing': True,
        'mysql_charset': 'urf-8'
    }

    def __str__(self):
        return self.user


class MessageBoard(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(255), nullable=False)
    mdatetime = db.Column(db.DateTime, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='messages')

    __table__args = {
        'extend_existing': True,
        'mysql_charset': 'utf-8'
    }

    def __str__(self):
        return self.content