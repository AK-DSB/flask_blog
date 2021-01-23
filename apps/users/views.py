import os
import time

from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, g
from sqlalchemy import and_
from werkzeug.utils import secure_filename
from apps.users.smssend import SmsSendAPIDemo

from apps.users.models import User, Photo, AboutMe, MessageBoard
from apps.articles.models import ArticleType, Article
from apps.utils.util import upload_qiniu, delete_qiniu, send_messages
from encryption import get_md5
from extends import db, cache
from settings import BaseConfig

user_bp = Blueprint('user', __name__, url_prefix='/user')

required_login_path = ['/user/center',
                       '/user/change',
                       '/article/publish',
                       '/user/upload_photo',
                       '/user/photo_del',
                       '/article/add_comment',
                       '/user/about_me',
                       '/user/show_about',
                       ]


@user_bp.before_app_first_request
def first_request():
    print('before_app_first_request')


@user_bp.before_app_request
def first_request1():
    print('before_first_request1:', request.path)
    if request.path in required_login_path:
        print('需要验证用户的登录情况')
        user_id = session.get('user_id')
        print(user_id)
        if not user_id:
            return render_template('user/login.html')
        else:
            user = User.query.get(user_id)
            # g对象，本次请求的对象，本次请求中产生的一个对象，存活周期只在这一次请求中
            g.user = user  # 给g对象添加一个user属性，属性值为 User.query.get(user_id)
            print('g:', g)


# 处理完了视图函数，拿到了一个返回值response对象
@user_bp.after_app_request
def after_request_test(response):
    response.set_cookie('username', 'AKW', max_age=19)
    print(response)
    print(request.cookies)
    return response


@user_bp.teardown_app_request
def teardown_request(response):
    return response


@user_bp.app_template_filter('cdecode')
def content_decode(content: bytes):
    content = content.decode('utf-8')
    return content[:200]


@user_bp.app_template_filter('cdecode1')
def content_decode1(content: bytes):
    return content.decode('utf-8')


@user_bp.route('/')
# @cache.cached(timeout=50)  # 缓存首页，50秒内返回首页时不需要发送请求
def index():
    print(request.cookies)
    # user_id = request.cookies.get('is_login', None)
    print('session:', session)

    user_id = session.get('user_id')
    print(user_id)
    # 接收页码数
    page = int(request.args.get('page', 1))
    pagination = Article.query.order_by(-Article.publish_date).paginate(page=page, per_page=3)  # 用于分页的函数paginate
    # Article.query.order_by(-Article.publish_date).all() 负号表示降序
    print(pagination.items)  # [<Article 4>, <Article 3>, <Article 2>],获取拿到的记录

    print(pagination.page)  # 当前的页码数
    print(pagination.prev_num)
    print(pagination.next_num)
    print(pagination.has_next)
    print(pagination.has_prev)
    print(pagination.pages)  # 总共可以分为几页
    print(pagination.total)  # 总共几条数据
    types = ArticleType.query.all()
    for i in range(10):
        time.sleep(0.5)
        if user_id:  # 判断用户是否登录
            user = User.query.get(user_id)
            return render_template('user/index.html', user=user, types=types, pagination=pagination)
        return render_template('user/index.html', types=types, pagination=pagination)


@user_bp.route('/register', endpoint='register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # con_password = generate_password_hash(request.form.get('confirmPassword'))
        con_password = get_md5(request.form.get('confirmPassword'))
        user_dic = {
            'username': request.form.get('username'),
            'password': get_md5(request.form.get('password')),
            'phone': request.form.get('phone'),
            'email': request.form.get('email')
        }
        if con_password == user_dic.get('password'):
            user = User(**user_dic)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login'))
        else:
            return redirect(url_for('user.register'))
    return render_template('user/register.html')


@user_bp.route('/login', endpoint='login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        f = request.args.get('f')
        if f == '1':
            username = request.form.get('username')
            password = get_md5(request.form.get('password'))
            users = User.query.filter(and_(User.username == username, User.password == password)).all()
            for user in users:
                if user:
                    # response = redirect(url_for('user.index'))
                    # response.set_cookie('is_login', value=str(user.id), max_age=600000)
                    # print(response)
                    # return response
                    session['user_id'] = user.id
                    print('session:', session)
                return redirect(url_for('user.index'))
            else:
                return render_template('user/login.html', msg='用户名或密码有误')
        elif f == '2':
            phone = request.form.get('phone')
            code = request.form.get('code')
            print('session:code:', session, code)
            # 先验证验证码
            valid_code = cache.get(phone)
            if code == valid_code:
                user = User.query.filter(User.phone == phone).first()
                if user:
                    # 登录成功, 记录登录成功的状态
                    session['user_id'] = user.id
                    return redirect(url_for('user.index'))
                else:
                    return render_template('user/login.html', msg='此号码未注册')
            else:
                return render_template('user/login.html', msg='验证码有误!')
    return render_template('user/login.html')


# 手机号码验证
@user_bp.route('/check_phone', endpoint='check', methods=['GET', 'POST'])
def check_phone():
    phone = request.args.get('phone')
    user = User.query.filter(User.phone == phone).all()
    # code: 400 不能用  200 可以用
    if len(user) > 0:
        return jsonify(code=400, msg='此手机号码以被注册')
    else:
        return jsonify(code=200, msg='此号码可以用')


@user_bp.route('/send_msg', endpoint='send_msg')
def send_message():
    phone = request.args.get('phone')
    """示例代码入口"""
    ret, code = send_messages(phone)
    print('ret:ret:ret:ret:ret:ret:ret:ret:', ret, code)
    if ret is not None:
        if ret['code'] == 405:
            # 存到缓存redis
            # cache.set(key, value, timeout=second)
            cache.set(phone, code, timeout=180)
            return jsonify(code=ret['code'], msg=f'验证码为{code}，请在3分钟之内填写，短信服务尚未通过审核，敬请谅解')
        else:
            print(f'ERROR: ret.code={ret["code"]},msg={ret["msg"]}')
            return jsonify(code=400, msg='短信发送失败')


@user_bp.route('/logout', endpoint='logout')
def logout():
    # 通过response对象删除cookie
    # response = redirect(url_for('user.index'))
    # print(response)
    # response.delete_cookie('is_login')
    del session['user_id']  # 指回删除session中的这个键值对  不会删除session空间和cookie
    session.clear()  # session.clear() 删除session的内存空间和删除cookie
    return redirect(url_for('user.index'))


# 用户中心
@user_bp.route('/center', endpoint='center')
def user_center():
    types = ArticleType.query.all()
    photos = Photo.query.filter(Photo.user_id == g.user.id).all()
    return render_template('user/center.html', user=g.user, types=types, photos=photos)


# 图片扩展名
ALLOWED_EXTENSIONS = ['jpg', 'png', 'gif', 'bmp']


# 用户信息修改
@user_bp.route('/change', methods=['GET', 'POST'], endpoint='change')
def user_change():
    if request.method == 'POST':
        icon = request.files.get('icon')
        icon_name = icon.filename
        suffix = icon_name.rsplit('.')[-1]
        if suffix in ALLOWED_EXTENSIONS:
            icon_name = secure_filename(icon_name)  # 保证文件名是符合python的命名规则
            file_path = os.path.join(BaseConfig.UPLOAD_ICON_DIR, icon_name)
            icon.save(file_path)
            path = 'upload/icon/'

            username = request.form.get('username')
            phone = request.form.get('phone')
            email = request.form.get('email')

            user = g.user
            user.username = username
            user.phone = phone
            user.email = email
            user.icon = os.path.join(path, icon_name)
            db.session.commit()
            return redirect(url_for('user.center'))
        else:
            return render_template('user/center.html', user=g.user, msg='请上传图片，格式为jpg,png,bmp,gif')
        # 判断手机号是否已注册或被使用
        # users = User.query.all()
        # for user in users:
        #     if user.phone == phone:
        #         # 改号码已被使用
        #         return render_template('user/center.html', user=g.user, msg='此号码已被使用')

    return render_template('user/center.html', user=g.user, types=ArticleType.query.all())


@user_bp.route('/upload_photo', methods=['GET', 'POST'])
def upload_photo():
    # 获取上传的内容
    photo_file = request.files.get('photo')
    print(photo_file)
    ret, info = upload_qiniu(photo_file)
    key = ret['key']
    if info.status_code == 200:
        photo_dic = {
            'photo_name': key,
            'user_id': g.user.id
        }
        photo = Photo(**photo_dic)
        db.session.add(photo)
        db.session.commit()
        return '上传成功'
    else:
        return '上传失败'


# 删除相册图片
@user_bp.route('/photo_del')
def photo_del():
    pid = request.args.get('pid')
    photo = Photo.query.get(pid)
    ret, info = delete_qiniu(photo)
    if info.status_code == 200:
        # 删除数据库中的图片
        db.session.delete(photo)
        db.session.commit()
        return redirect(url_for('user.center'))
    else:
        refer = request.referrer  # 也可以通过request.headers.get('Referer', None) 获取
        print(refer)
        return render_template('500.html', err_msg='删除相册图片失败', refer=refer)


@user_bp.route('/myphoto')
def myphoto():
    print('referer:', request.referrer)
    page = int(request.args.get('page', 1))
    pagination = Photo.query.paginate(page=page, per_page=3)
    user_id = session.get('user_id')
    user = None
    if user_id:
        user = User.query.get(user_id)
    return render_template('user/myphoto.html', pagination=pagination, user=user)


@user_bp.route('/about_me', methods=['GET', 'POST'], endpoint='about')
def about_me():
    try:
        about_dic = {
            'content': request.form.get('about').encode('utf-8'),
            'user_id': g.user.id  # 字段唯一，所以要添加异常处理
        }
        about_me = AboutMe(**about_dic)
        db.session.add(about_me)
        db.session.commit()
        types = ArticleType.query.all()
        return render_template('user/about_me.html', user=g.user, types=types)
    except Exception as e:
        print(e)
        return redirect(url_for('user.center'))


@user_bp.route('/show_about')
def show_about():
    types = ArticleType.query.all()
    user = session.get('user_id')
    return render_template('user/about_me.html', user=g.user, types=types)


@user_bp.route('/board', methods=['GET', 'POST'])
def show_board():
    user_id = session.get('user_id', None)
    user = None
    page = int(request.args.get('page', 1))
    pagination = MessageBoard.query.order_by(-MessageBoard.mdatetime).paginate(page=page, per_page=5)
    if user_id:
        user = User.query.get(user_id)
    if request.method == 'POST':
        message_dic = {
            'content': request.form.get('board'),
        }
        if user_id:
            message_dic.update(user_id=user_id)
        message = MessageBoard(**message_dic)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('user.show_board'))

    return render_template('user/board.html', user=user, types=ArticleType.query.all(), boards=pagination)


@user_bp.route('/board_del')
def delete_board():
    bid = request.args.get('bid')
    if bid:
        msgboard = MessageBoard.query.get(bid)
        db.session.delete(msgboard)
        db.session.commit()
        return redirect(url_for('user.center'))