from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileAllowed

class ArticleForm(FlaskForm):
    title = StringField("Article Name", validators=[DataRequired(),Length(min=5,max=255)])
    article_img = FileField("imagefield",validators=[FileAllowed(['jpg','png'])]) 
    content = TextAreaField("AContent", validators=[DataRequired(),Length(min=100,max=1000)])
    submit = SubmitField("Submit")