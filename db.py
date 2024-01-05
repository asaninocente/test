from app import db, Persona, app

with app.app_context():
    db.create_all()

    persona1 = Persona("Antonio", 34)
    persona2 = Persona("Juan", 30)

    db.session.add_all([persona1, persona2])
    db.session.commit()

    persona3 = Persona("Maria", 20)
    db.session.add(persona3)
    db.session.commit()

    personas = Persona.query.all()
    print("Consultar todas las personas")
    print(personas)

    filtro1 = Persona.query.filter_by(nombre="Antonio")
    print("Filtro por nombre = Antonio")
    print(filtro1.all())

    seleccion1 = Persona.query.get(1)
    print("Búsqueda por id")
    print(seleccion1)

    persona = Persona.query.get(1)
    persona.edad = 45
    db.session.add(persona)
    db.session.commit()

    persona_borrar = Persona.query.get(3)
    db.session.delete(persona_borrar)
    db.session.commit()
    print("Hemos borrado esta persona {}".format(persona_borrar))

    personas = Persona.query.all()
    print("Todas las personas")
    print(personas)