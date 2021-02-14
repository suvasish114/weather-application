from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    city_name = StringField('City Name', validators=[DataRequired()])
    search_btn = SubmitField('Search')