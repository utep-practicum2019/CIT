from database import Database

class DatabaseHandler:
    @staticmethod
    def insert(collection_name, document_id, document):
        return Database.insert(collection_name, document_id, document)

    @staticmethod
    def find(collection_name, document_id=None):
        return Database.find(collection_name, document_id)

    @staticmethod
    def update(collection_name, document_id, update):
        return Database.update(collection_name, document_id, update)

    @staticmethod
    def delete_document(collection_name, document_id):
        # TODO: merge with delete_collection
        return Database.delete_document(collection_name, document_id)

    @staticmethod
    def delete_collection(collection_name):
        return Database.delete_collection(collection_name)

    @staticmethod
    def create(collection_name):
        return Database.create(collection_name)
