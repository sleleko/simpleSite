from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Вход')


class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя ', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Еще раз пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Зарегистрироваться")


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Данное имя пользователя занято, выберите другое')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Пользователь с таким E-mail уже есть, выберите другой E-mail')


class ContactForm(FlaskForm):
    name = StringField('Ваше имя (*)', validators=[DataRequired()])
    email = StringField('E-mail (*)', validators=[DataRequired()])
    msg = TextAreaField('Текст вашего сообщения (*)', validators=[DataRequired()])
    submit = SubmitField("Отправить сообщение")