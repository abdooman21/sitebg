from webapp.forms.ArticleForm import ArticleForm
from webapp.models.ArticleModel import Article
from flask import redirect, url_for,render_template

class ArticleController:
    def article_add():
        form = ArticleForm()
        if form.validate_on_submit():
            new_article = Article(user_id=1, title= form.title.data,content= form.content.data)
            # store in db 

            return redirect("main_controller.home")
        
        return render_template("article/article_add.jinja",form=form, legend="Add New article", title = "add article")
    