"""
    This is a STUB
    TODO: Implementation  and integration is needed with database for deliverable #3
"""


class Database:
    group1 = {'group_id': 1, 'min_members': 11, 'max_members': 111}
    group2 = {'group_id': 2, 'min_members': 22, 'max_members': 222}
    group3 = {'group_id': 3, 'min_members': 33, 'max_members': 333}
    groups = {1: group1, 2: group2, 3: group3}
    user1 = {'username': 'user1', 'password': 'pass1'}
    user2 = {'username': 'user2', 'password': 'pass2'}
    user3 = {'username': 'user3', 'password': 'pass3'}
    users = {1:user1, 2:user2, 3:user3}
    db = {'users': users, 'groups': groups}

    @staticmethod
    def create(collection_name):
        # TODO: implement and intergrate create with database
        try:
            Database.db[collection_name]
            return False
        except KeyError:
            Database.db[collection_name] = {}
            return True

    @staticmethod
    def insert(collection_name, document_id, document):
        # TODO: implement and intergrate insert with database
        try:
            Database.db[collection_name][document_id] = document
            return True
        except KeyError:
            return False

    @staticmethod
    def find(collection_name, document_id):
        # TODO: implement and intergrate find with database
        try:
            return Database.db[collection_name][document_id]
        except KeyError:
            return  False

    @staticmethod
    def delete_collection(collection_name):
        # TODO: implement and intergrate delete_collection with database
        try:
            del Database.db[collection_name]
            return True
        except KeyError:
            return  False

    @staticmethod
    def delete_document(collection_name, document_id):
        # TODO: implement and intergrate delete_document with database
        try:
            del Database.db[collection_name][document_id]
            return True
        except KeyError:
            return False

