from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    genre = StringField('Genre')
    publication_date = StringField('Publication Date')
    isbn = StringField('ISBN')
    cover_image_url = StringField('Cover Image URL')
    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):
    content = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')

