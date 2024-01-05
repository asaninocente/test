#from flask_bcrypt import Bcrypt
from login import app, db
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from login.modelos import Usuario
from login.formulario import FormularioRegistro, FormularioLogin
from werkzeug.security import generate_password_hash, check_password_hash

#generador = Bcrypt()

#password = 'clavesecreta1'
#password_encriptada = generador.generate_password_hash(password)
#print(password_encriptada)

#verificar = generador.check_password_hash(password_encriptada, 'clavesecreta1')
#print(verificar)

#password = 'clavesecreta2'
#password_encriptada = generate_password_hash(password)
#print(password_encriptada)

#verificar = check_password_hash(password_encriptada, 'clavesecreta2')
#print(verificar)



@app.route('/')
def principal():
    return render_template('principal.html')

@app.route('/bienvenido')
@login_required
def bienvenido():
    return render_template('bienvenida.html')

@app.route('/salir')
@login_required
def salir():
    logout_user()
    flash('Sesión de usuario cerrada')
    return render_template('bienvenida.html')

@app.route('/entrar', methods=['GET', 'POST'])
def entrar():
    formulario = FormularioLogin()
    if formulario.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formulario.email.data).first()
        if usuario is not None:
            if check_password_hash(usuario.pass_hash, formulario.password.data):
                login_user(usuario)
                flash("Inicio de sesión correcto")
                proxima = request.args.get('next')
                if proxima == None or not next[0] == '/':
                    proxima = url_for('bienvenido')
                return redirect(proxima)
    return render_template('entrar.html', formulario=formulario)

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    formulario = FormularioRegistro()
    if formulario.validate_on_submit():
        usuario = Usuario(email=formulario.email.data, nombre=formulario.nombre.data, password=formulario.password.data)
        db.session.add(usuario)
        db.session.commit()
        flash("Usuario registrado correctamente")
        return redirect(url_for('entrar'))
    return render_template('registrar.html', formulario=formulario)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")