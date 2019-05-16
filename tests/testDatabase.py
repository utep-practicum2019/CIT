import requests, json, unittest
import json as simplejson

#Test Database API

database_url = "http://citsystem.com/api/v2/resources/database"

class test_Database(unittest.TestCase):

    def test_getDatabase(self):
        data = {
                "collection_name" : "groups",
                "document_id" : 5
                }
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.get(database_url, json=data)
        print(r.text)
        self.assertIn("group_id", r.text)
 

    def test_getDatabase_no_input(self):
        data = {}
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.get(database_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_getDatabase_missing_fields(self):
        data = {
                "collection_name" : "groups"
                }
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.get(database_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)

    def test_getDatabase_inexistent_collection(self):
        data = {
                "collection_name" : "gps",
                "document_id" :100
                }
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.get(database_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)

    def test_create_collection(self):
        data = {
                "collection_name" : "groups",
                "document_id" : 4,
                "document" :  {
                    "group_id": 4,
                    "min": 5,
                    "max": 8,
                    "platforms": ["TiddlyWiki"],
                    "members": [
                        "Pedro",
                        "user79",
                        "user88"
                    ]
                }
                }
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.post(database_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_create_collection_no_input(self):
        data = {}
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.post(database_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_create_collection_missing_fields(self):
        data = {
                "collection_name" : "groups",
                "document_id" : 7
                }
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.post(database_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)

    def test_create_invalid_collection(self):
        data = {
                "collection_name" : "groups",
                "document_id" : 7,
                "document" :  {
                    "other_id": 7,
                    "users": ["TiddlyWiki"]
                }
                }
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.post(database_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)

    def test_update_collection(self):
        data = {
                "collection_name" : "groups",
                "document_id" : 1,
                "document" :  {
                    "group_id": 1,
                    "min": 3,
                    "max": 8,
                    "platforms": ["Rocketchat"],
                    "members": [
                        "Pedro10",
                        "user79",
                        "user88"
                    ]
                }
                }
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.put(database_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_update_collection_no_input(self):
        data = {}
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.put(database_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_update_collection_missing_fields(self):
        data = {
                "document_id" : 3,
                "document" :  {
                    "group_id": 3,
                    "min": 3,
                    "max": 8,
                    "platforms": ["TiddlyWiki", "Rocketchat"],
                    "members": [
                        "Pedro10",
                        "user79",
                        "user88"
                    ]
                }
                }
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.put(database_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)

    def test_update_inexistent_collection(self):
        data = {
                "collection_name" : "other",
                "document_id" : 18,
                "document" :  {
                    "group_id": 18,
                    "min": 3,
                    "max": 8,
                    "platforms": ["wiki"],
                    "members": [
                        "Pedro10",
                        "user79",
                        "user88"
                    ]
                }
                }
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.put(database_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)

    def test_delete_colection(self):
        data = {
                "collection_name" : "groups",
                "document_id" : 6
                }
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.delete(database_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_delete_colection_no_input(self):
        data = {}
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.delete(database_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_delete_colection_missing_fields(self):
        data = {
            "collection_name": "groups"
        }
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.delete(database_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)

    def test_delete_inexistent_colection(self):
        data = {
            "collection_name": "gps",
            "document_id": 24
        }
        #local_url = "http://localhost:5000/api/v2/resources/database"
        r = requests.delete(database_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)


if __name__ == '__main__':
    print ("TEST - Database API")
    unittest.main()

