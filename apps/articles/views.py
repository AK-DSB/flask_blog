from flask import Blueprint, request, session, g, redirect, url_for, render_template, jsonify, session
from apps.articles.models import Article, ArticleType, Comment
from apps.users.models import User
from extends import db

article_bp = Blueprint('article', __name__)


@article_bp.route('/publish', methods=['POST', 'GET'], endpoint='publish')
def publish_article():
    if request.method == 'POST':
        article_dic = {
            'title': request.form.get('title'),
            'content': request.form.get('content').encode('utf-8'),
            'type_id': request.form.get('type'),
            'user_id': g.user.id,
        }
        article = Article(**article_dic)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('user.index'))


@article_bp.route('/detail', endpoint='detail')
def article_detail():
    article_id = request.args.get('article_id')
    article = Article.query.get(article_id)
    types = ArticleType.query.all()
    user_id = session.get('user_id')  # 登录用户
    user = None
    if user_id:
        user = User.query.get(user_id)
    # 单独查询评论
    page = int(request.args.get('page', 1))
    pagination = Comment.query.filter(Comment.article_id == article_id).order_by(-Comment.comment_date).paginate(page=page, per_page=5)
    return render_template('article/detail.html', article=article, types=types, user=user, pagination=pagination)


@article_bp.route('/save', endpoint='save')
def article_love():
    article_id = request.args.get('article_id')
    tag = request.args.get('tag')
    article = Article.query.get(article_id)
    if tag == '1':
        article.save_num -= 1
    else:
        article.save_num += 1
    db.session.commit()
    return jsonify(num=article.save_num)


@article_bp.route('/love', endpoint='love')
def article_love():
    tag = request.args.get('tag')
    article_id = request.args.get('article_id')
    article = Article.query.get(article_id)
    if tag == '1':
        article.love_num -= 1
    else:
        article.love_num += 1
    db.session.commit()
    return jsonify(num=article.love_num)


@article_bp.route('/add_comment', methods=['GET', 'POST'])
def article_comment():
    if request.method == 'POST':
        comment_dic = {
            'comment': request.form.get('comment'),
            'user_id': g.user.id,
            'article_id': request.form.get('aid')
        }
        comment = Comment(**comment_dic)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('article.detail', article_id=comment_dic.get('article_id')))
    return redirect(url_for('user.index'))


@article_bp.route('/type_search')
def type_search():
    user_id = session.get('user_id')
    user = None
    if user_id:
        user = User.query.get(user_id)
    types = ArticleType.query.all()
    type_id = request.args.get('type_id', 1)
    article_type = ArticleType.query.get(type_id)

    return render_template('article/article_type.html', user=user, types=types, article_type=article_type)