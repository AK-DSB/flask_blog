from flask import Blueprint, render_template, request, redirect, url_for
from flask_blog.apps.users import models as user_model
from flask_blog.apps.articles import models as article_model
from flask_blog.extends import db

article_bp = Blueprint('article', __name__)


@article_bp.route('/publish', endpoint='publish', methods=['GET', 'POST'])
def publish_article():
    if request.method == 'POST':
        print('****************************')
        print(request.form)
        article_dic = {
            'title': request.form.get('title'),
            'content': request.form.get('content'),
            'user_id': request.form.get('user_id')
        }
        # 添加文章
        article = article_model.Article(**article_dic)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('article.publish'))
    else:
        users = user_model.User.query.filter(user_model.User.is_delete == False).all()
        return render_template('article/add_article.html', users=users)


@article_bp.route('/all', endpoint='all')
def all_article():
    articles = article_model.Article.query.all()
    return render_template('article/all.html', articles=articles)


@article_bp.route('/all1')
def all_artilce1():
    id = request.args.get('id')
    user = user_model.User.query.get(id)
    return render_template('article/all1.html', user=user)













































