from app import db, Persona, app

with app.app_context():
    persona = Persona.query.get(1)
    persona.color = "verde"
    db.session.add(persona)
    db.session.commit()

    personas = Persona.query.all()
    print(personas)