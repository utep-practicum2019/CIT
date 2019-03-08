import unittest

from Database.database_handler import DatabaseHandler


class TestDatabaseMethods(unittest.TestCase):
    def test_find_user_no_doc_id(self):
        collection_name = "users"
        document_id = None
        self.assertTrue(DatabaseHandler.find(collection_name, document_id))

    def test_find_user(self):
        collection_name = "users"
        document_id = "Pedro"
        document = {"username": "Pedro"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertEqual(DatabaseHandler.find(collection_name, document_id), document)

    def test_find_missing_user(self):
        collection_name = "users"
        document_id = "Pedro"
        self.assertFalse(DatabaseHandler.find(collection_name, document_id))
		
    def test_find_group(self):
        collection_name = "groups"
        document_id = "1"
        document = {"group_id": "1"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertEqual(DatabaseHandler.find(collection_name, document_id), document)

    def test_find_missing_group(self):
        collection_name = "groups"
        document_id = "1"
        document = {"group_id": "1"}
        self.assertFalse(DatabaseHandler.find(collection_name, document_id))
		
    def test_find_platform(self):
        collection_name = "platforms"
        document_id = "Rocketchat"
        document = {"platforms": "Rocketchat"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertEqual(DatabaseHandler.find(collection_name, document_id), document)

    def test_find_missing_platform(self):
        collection_name = "platforms"
        document_id = "Rocketchat"
        document = {"platforms": "Rocketchat"}
        self.assertFalse(DatabaseHandler.find(collection_name, document_id))

    def test_insert_user(self):
        collection_name = "users"
        document_id = "Pedro"
        document = {"username": "Pedro"}
        self.assertTrue(DatabaseHandler.insert(collection_name, document_id, document))

    def test_insert_existing_user(self):
        collection_name = "Test"
        document_id = "Pedro"
        document = {"username": "Pedro"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertFalse(DatabaseHandler.insert(collection_name, document_id, document))

    def test_insert_group(self):
        collection_name = "groups"
        document_id = "1"
        document = {"group_id": "1"}
        self.assertTrue(DatabaseHandler.insert(collection_name, document_id, document))

    def test_insert_existing_group(self):
		collection_name = "groups"
        document_id = "1"
        document = {"group_id": "1"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertFalse(DatabaseHandler.insert(collection_name, document_id, document))
		
    def test_insert_platform(self):
        collection_name = "platforms"
        document_id = "Rocketchat"
        document = {"platforms": "Rocketchat"}
        self.assertTrue(DatabaseHandler.insert(collection_name, document_id, document))
	
    def test_insert_existing_platform(self):
        collection_name = "platforms"
        document_id = "Rocketchat"
        document = {"platforms": "Rocketchat"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertFalse(DatabaseHandler.insert(collection_name, document_id, document))
		
	def test_update_user(self):
        collection_name = "users"
        document_id = "Pedro"
        document = {"username": "Pedro"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertTrue(DatabaseHandler.update(collection_name, document_id, document))

    def test_update_missing_user(self):
        collection_name = "users"
        document_id = "Pedro"
        document = {"username": "Pedro"}
        self.assertFalse(DatabaseHandler.update(collection_name, document_id, document))

	def test_update_group(self):
		collection_name = "groups"
        document_id = "1"
        document = {"group_id": "1"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertTrue(DatabaseHandler.update(collection_name, document_id, document))

    def test_update_missing_group(self):
		collection_name = "groups"
        document_id = "1"
        document = {"group_id": "1"}
        self.assertFalse(DatabaseHandler.update(collection_name, document_id, document))

	def test_update_platform(self):
        collection_name = "platforms"
        document_id = "Rocketchat"
        document = {"platforms": "Rocketchat"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertTrue(DatabaseHandler.update(collection_name, document_id, document))

    def test_update_missing_platform(self):
        collection_name = "platforms"
        document_id = "Rocketchat"
        document = {"platforms": "Rocketchat"}
        self.assertFalse(DatabaseHandler.update(collection_name, document_id, document))

    def test_delete_drop_table(self):
        collection_name = "users"
        document_id = None
        document = {"username": None}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertTrue(DatabaseHandler.delete(collection_name, document_id))

    def test_delete_user(self):
        collection_name = "users"
        document_id = "Pedro"
        document = {"username": "Pedro"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertTrue(DatabaseHandler.delete(collection_name, document_id))

    def test_delete_missing_user(self):
        collection_name = "users"
        document_id = "Pedro"
        self.assertFalse(DatabaseHandler.delete(collection_name, document_id))

    def test_delete_group(self):
		collection_name = "groups"
        document_id = "1"
        document = {"group_id": "1"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertTrue(DatabaseHandler.delete(collection_name, document_id))

    def test_delete_missing_group(self):
 		collection_name = "groups"
        document_id = "1"
        document = {"group_id": "1"}
        self.assertFalse(DatabaseHandler.delete(collection_name, document_id))

    def test_delete_platform(self):
        collection_name = "platforms"
        document_id = "Rocketchat"
        document = {"platforms": "Rocketchat"}
        DatabaseHandler.insert(collection_name, document_id, document)
        self.assertTrue(DatabaseHandler.delete(collection_name, document_id))

    def test_delete_missing_platform(self):
        collection_name = "platforms"
        document_id = "Rocketchat"
        document = {"platforms": "Rocketchat"}
        self.assertFalse(DatabaseHandler.delete(collection_name, document_id))



if __name__ == '__main__':
    unittest.main()
