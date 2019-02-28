"""
    TODO: Implementation  and integration for platforms
    TODO: Testing with users
    TODO: Testing with groups
    Platforms shouldn't change it much because it's pretty generic.
"""

from pymongo import MongoClient

class Database:
    __client = MongoClient('localhost', 27017)
    __db = __client['cit']
    __users = __db['users']
    __groups = __db['groups']
    collection = {
        'users': __users,
        'groups': __groups
    }

    @staticmethod
    def insert(collection_name, document_id, document):
        try:
            if Database.find(collection_name, document_id):
                return False
            Database.collection[collection_name].insert_one(document)
            return True
        except KeyError:
            return False

    @staticmethod
    def find(collection_name, document_id):
        # TODO: determine if you should return just the usernames or all the user info
        try:
            if document_id is None:
                cursor = Database.collection[collection_name].find()
                users = []
                while True:
                    try:
                        user = cursor.next()
                        del user['_id']
                        users.append(user)
                    except StopIteration:
                        return users
            doc = Database.collection[collection_name].find_one(document_id)
            if doc is not None:
                del doc['_id']
            return doc
        except KeyError:
            return False

    @staticmethod
    def update(collection_name, document_id, document):
        try:
            setter = {'$set': document}
            old_doc = Database.collection[collection_name].find_one_and_update(document_id, setter)
            if old_doc is not None:
                del old_doc['_id']
            return old_doc
        except KeyError:
            return False

    @staticmethod
    def delete_document(collection_name, document_id):
        # TODO: merge with delete_collection()
        try:
            del_doc = Database.collection[collection_name].find_one_and_delete(document_id)
            if del_doc is not None:
                del del_doc['_id']
            return del_doc
        except KeyError:
            return False

    @staticmethod
    def delete_collection(collection_name):
        # TODO: implement and intergrate delete_collection with database
        # might not actually have to implement this method
        return False

    @staticmethod
    def create(collection_name):
        # TODO: implement and intergrate create with database
        # might not actually have to implement this method
        return False
