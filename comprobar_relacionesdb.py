from relacionesdb import db, Mascota, Juguete, Propietario, app

with app.app_context():
    mascota1 = Mascota('Mia')
    mascota2 = Mascota('Bella')

    db.session.add_all([mascota1, mascota2])
    db.session.commit()

    mascotas = Mascota.query.all()
    print(mascotas)

    mascota1 = Mascota.query.filter_by(nombre='Mia').first()

    propietario1 = Propietario('Antonio', mascota1.id)
    db.session.add(propietario1)
    db.session.commit()

    juguete1 = Juguete('pelota', mascota1.id)
    juguete2 = Juguete('peluche', mascota1.id)
    db.session.add_all([juguete1, juguete2])
    db.session.commit()

    mascota = Mascota.query.filter_by(nombre='Mia').first()
    print(mascota)
    mascota.mostrar_juguetes()