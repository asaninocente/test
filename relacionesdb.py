import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir,'mascotas.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

class Mascota(db.Model):
    __tablename__ = 'Mascotas'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.Text)
    juguetes = db.relationship('Juguete',backref='mascota',lazy='dynamic')
    propietario = db.relationship('Propietario', backref='mascota', uselist=False)

    def __init__(self,nombre):
        self.nombre = nombre
    
    def __repr__(self):
        texto = "Mascota: nombre {}".format(self.nombre)
        return texto
    
    def mostrar_juguetes(self):
        for juguete in self.juguetes:
            print(juguete.nombre)

class Juguete(db.Model):
    __tablename__ = 'Juguetes'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.Text)
    mascota_id = db.Column(db.Integer, db.ForeignKey('Mascotas.id'))

    def __init__(self, nombre, mascota_id):
        self.nombre = nombre
        self.mascota_id = mascota_id

class Propietario(db.Model):
    __tablename__ = 'Propietarios'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.Text)
    mascota_id = db.Column(db.Integer, db.ForeignKey('Mascotas.id'))

    def __init__(self, nombre, mascota_id):
        self.nombre = nombre
        self.mascota_id = mascota_id