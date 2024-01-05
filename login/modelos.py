from login import db, gestor
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@gestor.user_loader
def load_user(Usuario_id):
    return Usuario.query.get(Usuario_id)

class Usuario(db.Model, UserMixin):
    __tablename__ = 'Usuarios'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    nombre = db.Column(db.String(64), unique=True, index=True)
    pass_hash = db.Column(db.String(128))

    def __init__(self, email, nombre, password):
        self.email = email
        self.nombre = nombre
        self.pass_hash = generate_password_hash(password)
    
    def verificar_password(self, password):
        return check_password_hash(self.pass_hash, password)