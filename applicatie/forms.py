from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class GrafiekForm(FlaskForm):
    mnd_keuzes = [(1, 'Januari'), (2, 'Februari'), (3, 'Maart'),(4,'April'),(5,'Mei'),(6,'Juni'),
                  (7, 'Juli'), (8, 'Augustus'), (9, 'September'),(10,'Oktober'),(11,'November'),(12,'December'),]
    jr_keuzes = [(2017 , '2017'), (2018,'2018'),(2019,'2019'),(2020,'2020')]
    maand = SelectField('Maand', coerce=int, choices=mnd_keuzes, validators=[DataRequired()])
    start_jaar = SelectField('Start jaar',  choices=jr_keuzes, validators=[DataRequired()])
    eind_jaar = SelectField('Eind jaar', choices=jr_keuzes, validators=[DataRequired()])
    tekst = 'Kijk, er staat een tekstje'
    submit = SubmitField('Start')