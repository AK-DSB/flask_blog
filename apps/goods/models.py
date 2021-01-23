from extends import db


class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    goods_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    # 因为用户和商品是多对多关系，无法直接添加外键，所以要依赖第三张关系表来建立relationship，secondary=第三张表表名
    # relationship里的backref的值可以随便起,用来反向引用
    users = db.relationship('User', backref='goods_list', secondary='user_goods')

    __table_args__ = {
        'extend_existing': True,
        'mysql_charset': 'utf8'
    }

    def __str__(self):
        return self.goods_name


# 创建多对多关系表----第一种方式
# tags = db.Table('tags',
#        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
#         db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
#     )


class UserGoods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id'))
    number = db.Column(db.Integer, default=1)

    __table_args = {
        'extend_existing': True,
        'mysql_charset': 'utf8'
    }