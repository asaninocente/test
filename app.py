import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

dir = os.path.abspath(os.path.dirname(__file__))
print(dir)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir,'datos.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

# Creación del modelo o base de datos
class Persona(db.Model):
    __tablename__ = 'Personas'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.Text)
    edad = db.Column(db.Integer)
    color = db.Column(db.Text)

    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def __repr__(self):
        texto = "Persona : nombre={}, edad={} y color={}".format(self.nombre,self.edad,self.color)
        return texto