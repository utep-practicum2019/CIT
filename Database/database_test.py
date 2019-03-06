import unittest

from Database.database_handler import DatabaseHandler


class TestDatabaseMethods(unittest.TestCase):

    def test_find_user(self):
        collection_name = "users"
        document_id = "Pedro1"
        document = {"username": "Pedro1"}
        DatabaseHandler.insert(collection_name, document_id, document)
        del document['_id']
        self.assertEqual(DatabaseHandler.find(collection_name, document_id), document)

    def test_find_missing_user(self):
        collection_name = "users"
        document_id = "Pedro2"
        self.assertFalse(DatabaseHandler.find(collection_name, document_id))

    def test_insert_user(self):
        collection_name = "users"
        document_id = "Pedro3"
        document = {"username": "Pedro3"}
        self.assertTrue(DatabaseHandler.insert(collection_name, document_id, document))

    def test_insert_existing_user(self):
        collection_name = "users"
        document_id = "Pedro4"
        document = {"username": "Pedro4"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertFalse(DatabaseHandler.insert(collection_name, document_id, document))

    def test_update_user(self):
        collection_name = "users"
        document_id = "Pedro5"
        document = {"username": "Pedro5"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertTrue(DatabaseHandler.update(collection_name, document_id, document))

    def test_update_missing_user(self):
        collection_name = "users"
        document_id = "Pedro6"
        document = {"username": "Pedro6"}
        self.assertFalse(DatabaseHandler.update(collection_name, document_id, document))

    def test_delete_user(self):
        collection_name = "users"
        document_id = "Pedro7"
        document = {"username": "Pedro7"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertTrue(DatabaseHandler.delete(collection_name, document_id))

    def test_delete_missing_user(self):
        collection_name = "users"
        document_id = "Pedro8"
        self.assertFalse(DatabaseHandler.delete(collection_name, document_id))

    def test_find_group(self):
        collection_name = "groups"
        document_id = 9
        document = {"group_id": 9}
        DatabaseHandler.insert(collection_name, document_id, document)
        del document['_id']
        self.assertEqual(DatabaseHandler.find(collection_name, document_id), document)

    def test_insert_group(self):
        collection_name = "groups"
        document_id = 10
        document = {"group_id": 10}
        self.assertTrue(DatabaseHandler.insert(collection_name, document_id, document))


if __name__ == '__main__':
    unittest.main()
