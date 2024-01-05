import os
from formulario import FormularioAlta, FormularioBaja
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'clavesecreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir,'gestion_mascotas.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

class Mascota(db.Model):
    __tablename__ = 'Mascotas'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.Text)

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        texto = "Mascota: nombre {}, id {}".format(self.nombre, self.id)
        return texto

# Vistas o rutas de la aplicación
@app.route('/')
def principal():
    return render_template('vista_principal.html')

@app.route('/lista')
def lista():
    mascotas = Mascota.query.all()
    return render_template('vista_lista.html', mascotas=mascotas)

@app.route('/alta', methods=['GET', 'POST'])
def alta():
    formulario = FormularioAlta()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        mascota = Mascota(nombre)
        db.session.add(mascota)
        db.session.commit()

        return redirect(url_for('lista'))
    return render_template('vista_alta.html', formulario=formulario)

@app.route('/baja', methods=['GET', 'POST'])
def baja():
    formulario = FormularioBaja()
    if formulario.validate_on_submit():
        id = formulario.id.data
        mascota_borrar = Mascota.query.get(id)
        db.session.delete(mascota_borrar)
        db.session.commit()

        return redirect(url_for('lista'))
    return render_template('vista_baja.html', formulario=formulario)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")