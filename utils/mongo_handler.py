from bson import ObjectId
import pymongo as mongo

if __name__ == '__main__':
    import connection_params
else:
    from . import connection_params


class MongoHandler:

    # a kapcsolathoz szükséges információk
    # egy fv ami a kapcsolatot létrehozza
    # egy fv ami lekér egy bizonyos adatot
    # lekér minden adatot
    # töröl adatot
    # módosít adatot


# refaktorákás része lesz a hiba kezelés
# python logging - logger

    def __init__(self):
        pass

    def get_mongo_database(self):
        uri = connection_params.params['uri']
        client = mongo.MongoClient(uri)
        database = client[connection_params.params['database']]

        return database

    def get_mongo_collection(self):
        return self.get_mongo_database()[connection_params.params["collection"]]

    def get_document(self, query):
        # query: valid query parameter ellenőrzés nincs
        # egyáltalán nem  fogolalkozom itt azzal, hogy a query hány találatot adna vissza
        coll = self.get_mongo_collection()

        return coll.find_one(query)

    def get_documents(self, query):
        # query: valid query parameter ellenőrzés nincs
        coll = self.get_mongo_collection()

        return coll.find(query)

    def delete_document(self, query):
        # query: valid query parameter ellenőrzés nincs
        # egyáltalán nem  fogolalkozom itt azzal, hogy a query hány találatot adna vissza
        coll = self.get_mongo_collection()

        return coll.delete_one(query)

    def update_document(self, query, update_statement, upsert=False):
        coll = self.get_mongo_collection()

        return coll.update_one(query, update_statement, upsert=upsert)

    def insert_document(self, document):
        coll = self.get_mongo_collection()

        return coll.insert_one(document).inserted_id


if __name__ == '__main__':
    db = MongoHandler()

    database = db.get_mongo_database()

    # for item in database['test_collection'].find({}):
    #     print(item)

    # for item in db.get_mongo_collection().find({}):
    #     print(item)

    query = {"_id" : ObjectId("61a66b627edd5e67b0324fb1")}
    #print(db.get_document(query))


    query = {}

    for item in db.get_documents(query):
        print(item)

    query = {"_id" : ObjectId("61a66b627edd5e67b0324fb1")}

    #db.delete_document(query)

    ##############################
    query = {"sütemény": "palacsita"} # update table set mezo = érték WHERE rész
    update_statement = {"$set": {"aperitif": "pálinka"}} # update table set mezo = érték

    # db.update_document(query, update_statement, True)