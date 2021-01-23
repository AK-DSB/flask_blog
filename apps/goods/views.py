from flask import Blueprint, render_template, redirect, url_for, request
from apps.users import models as user_model
from apps.goods import models as goods_model
from extends import db

goods_bp = Blueprint('goods', __name__)


# 根据用户找商品，查看用户买了哪些商品
@goods_bp.route('/find_goods', endpoint='find_goods')
def find_goods():
    user_id = request.args.get('user_id')
    user = user_model.User.query.get(user_id)
    return render_template('goods/find_goods.html', user=user)


# 根据商品找用户，哪些用户买了这件商品
@goods_bp.route('/find_user', endpoint='find_user')
def find_user():
    goods_id = request.args.get('goods_id')
    goods = goods_model.Goods.query.get(goods_id)
    return render_template("goods/find_user.html", goods=goods)


# 用户买商品
@goods_bp.route('/show', endpoint='show')
def show():
    if request.method == 'GET':
        users = user_model.User.query.filter(user_model.User.is_delete == False).all()
        goods_list = goods_model.Goods.query.all()
        context = {
            'users': users,
            'goods_list': goods_list
        }
        return render_template('goods/show.html', **context)
    else:
        return ''


@goods_bp.route('/buy', endpoint='buy')
def buy():
    user_id = request.args.get('user_id')
    goods_id = request.args.get('goods_id')
    user_goods = goods_model.UserGoods(user_id=user_id, goods_id=goods_id)
    print(user_id, goods_id, user_goods)
    db.session.add(user_goods)
    db.session.commit()
    u_g = goods_model.UserGoods.query.all()
    return render_template('goods/user_goods.html', u_g=u_g)