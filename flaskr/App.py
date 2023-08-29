from flaskr import create_app
from .modelos import db, Usuario, Album, Medio, Cancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    c = Cancion(titulo='prueba', minutos=2, segundos=25, interprete= 'Artista')
    u = Usuario(nombre='Alejo', contrasena='Alejo254')
    a = Album(titulo="Aventuras maquiavelicas", anio='1980', descripcion='Lo mejor de los mejor', medio=Medio.CD)
    a.canciones.append(c)
    u.albumes.append(a)
    db.session.add(u)
    db.session.add(a)
    db.session.commit()
    print(Usuario.query.all())
    print(Usuario.query.all()[0].albumes)
    db.session.delete(u)
    print(Album.query.all())
    print(Cancion.query.all())
