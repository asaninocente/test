from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class FormularioRegistro(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_repetir = PasswordField('Repetir password', validators=[DataRequired(),EqualTo('password_repetir', message="Las passwords no coinciden")])
    boton = SubmitField('Registrar')

    def verificar_mail(self, parametro):
        if Usuario.query.filter_by(email=parametro.data).first():
            raise ValidationError('Error. Este mail ya ha sido utilizado')
    
    def verificar_nombre(self, parametro):
        if Usuario.query.filter_by(nombre=parametro.data).first():
            raise ValidationError('Error. Este nombre ya ha sido utilizado')

class FormularioLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    boton = SubmitField('Entrar')