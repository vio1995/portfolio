from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import Email, Length, DataRequired, InputRequired

class Contact(FlaskForm):
    name = StringField("Nome", validators=[DataRequired(), Length(min=2, max=100)])
    subject = StringField("Assunto", validators=[DataRequired(), Length(min=2, max=100)])
    email = EmailField("E-mail", validators=[DataRequired(), Email()])
    message = TextAreaField("Mensagem", validators=[InputRequired()])
    submit = SubmitField('Enviar mensagem')