from database import Database

class DatabaseHandler:
    # TODO: sort out how the response will be given to the request handler i.e. replace prints

    @staticmethod
    def create(collection_name):
        if Database.create(collection_name):
            print("Success")
        else:
            print("False")

    @staticmethod
    def insert(collection_name, document_id, document):
        if Database.insert(collection_name, document_id, document):
            print("Success")
        else:
            print("False")

    @staticmethod
    def find(collection_name, document_id):
        doc = Database.find(collection_name, document_id)
        if doc:
            print("Success")
            return doc
        else:
            print("False")

    @staticmethod
    def delete_collection(collection_name):
        if Database.delete_collection(collection_name):
            print("Success")
        else:
            print("False")

    @staticmethod
    def delete_document(collection_name, document_id):
        if Database.delete_document(collection_name, document_id):
            print("Success")
        else:
            print("False")

    @staticmethod
    def getDB():
        # TODO: remove this method
        return Database.db
