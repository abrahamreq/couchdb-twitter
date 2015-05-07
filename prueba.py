import couchdb
import couchdb.design as diseno

couch = couchdb.Server()

try:
    db = couch['manolito']
except:
    db = couch.create("manolito")

def almacena():
    doc = {"Nombre" : "Antonio" , "Apellidos": "Lozano Barrera", "Profesion": "Agricultor", "DNI":"44444444s"}
    db.save(doc)

    for doc in db:
        print doc
        print db[doc]['Nombre']

def vista_nombre():
    nombre = '''function(doc) { if(doc.Nombre == "Antonio") { \
                if(doc.DNI) {
                emit (doc.Nombre, {"Nombre": doc.Nombre , "Apellidos":doc.Apellidos }); \
                } else { 
                emit (doc._id, doc); \
                } \
                } } '''
    view = diseno.ViewDefinition('prueba', 'vista', nombre)
    view.sync(db)

def nombre():
    return db.view('prueba/nombre')

if(__name__ == "__main__"):
    vista_nombre()
    for n in nombre():
        print n
