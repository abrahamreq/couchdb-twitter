import couchdb

couch = couchdb.Server()
db = couch.get_or_create('python-test')

doc_id, doc_rev = db.save({'type': 'Person', 'name': 'John Doe'})
    
doc = db[doc_id]
tipo = doc['type']
nombre = doc['name']
print doc
print tipo, nombre
del db[doc_id]
