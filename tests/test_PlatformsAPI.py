import requests, json, unittest
import json as simplejson

#Test Platforms API

users_url = "http://citsystem.com/api/v2/resources/platform"

class test_PlatformAPI(unittest.TestCase):
    # # Test Platform API
    def test_get_platform_no_input(self):
        print('Test platform | (GET) No input')
        data = {}
        r = requests.get(users_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_get_platform_status(self):
        print('Test platform status | (GET) All required fields')
        s_url = "http://citsystem.com/api/v2/resources/platform?status=True&platform_ID=41337"
        r = requests.get(s_url, json=data)
        print(r.text)
        self.assertIn("Running", r.text)

    def test_get_platform_status_missing_fields(self):
        print('Test platform status | (GET) missing fields')
        s_url = "http://citsystem.com/api/v2/resources/platform?status=True"
        r = requests.get(s_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)

    def test_get_platform_status_wrong_fields(self):
        print('Test platform status| (GET) Wrong fields')
        s_url = "http://citsystem.com/api/v2/resources/platform?status=True&platform_ID=41"
        r = requests.get(s_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)

    def test_get_available_plugins_true(self):
        print('Test available plugins| (GET) All required fields')
        s_url = "http://citsystem.com/api/v2/resources/platform?all=True"
        r = requests.get(s_url, json=data)
        print(r.text)
        self.assertIn("subplatforms", r.text)

    def test_get_available_plugins_false(self):
        print('Test available plugins| (GET) All required fields')
        s_url = "http://citsystem.com/api/v2/resources/platform?all=False"
        r = requests.get(s_url, json=data)
        print(r.text)
        self.assertIn("sub_platforms", r.text)
        self.assertIn("main_platforms", r.text)

    def test_create_platform_no_input(self):
        print('Test create platform | (Post) no input ')
        data = {}
        r = requests.post(users_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_create_platform(self):
        print('Test create platform | (Post) all fields')
        data = {"main_platform" : "Hackathon",
	            "subplatforms" : ["Rocketchat", "TiddlyWiki"]
                }
        r = requests.post(users_url, json=data)
        print(r.text)
        self.assertIn("Success", r.text)

    def test_create_platform_wrong_fields(self):
        print('Test create platform | (Post) wrong fields')
        data = {"main_platform" : "Results",
	            "subplatforms" : ["Rocketchat", "Wiki"]
                }
        r = requests.post(users_url, json=data)
        print(r.text)
        self.assertIn("Failure", r.text)

    def test_create_platform_missing_fields(self):
        print('Test create platform | (Post) missing fields ')
        data = {"main_platform" : "Results",
	            "subplatforms" : ["Rocketchat", "Wiki"]
                }
        r = requests.post(users_url, json=data)
        print(r.text)
        self.assertIn("Failure", r.text)

    def test_add_platform_no_input(self):
        print('Test add platform | (Post) no input ')
        data = {}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_add_platform(self):
        print('Test add platform | (Post) all fields')
        data = {"platform_ID": 41163,
	            "subplatforms" : ["Rocketchat"]
                }
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("Success", r.text)

    def test_add_platform_wrong_fields(self):
        print('Test add platform | (Post) wrong fields')
        data = {"platform_ID": 5,
	            "subplatforms" : ["Rocketchat"]
                }
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("Failure", r.text)

    def test_add_platform_missing_fields(self):
        print('Test add platform | (Post) missing fields')
        data = {"platform_ID": 41163
                }
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)

    def test_start_platform_no_input(self):
        print('Test start platform | (Put) ')
        data = {}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_start_platform(self):
        print('Test start platform | (Put) all fields ')
        data = {"command" : "start",
	            "platform_ID" : 58585,
	            "subplatforms_IDS" : [52994, 53033]}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("Success", r.text)

    def test_start_platform_wrong_fields(self):
        print('Test start platform | (Put) wrong fields ')
        data = {"command" : "start",
	            "platform_ID" : 585,
	            "subplatforms_IDS" : [524, 53]}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)

    def test_start_platform_missing_fields(self):
        print('Test start platform | (Put) missing fields ')
        data = {"command" : "start",
	            "platform_ID" : 58585}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)

    def test_stop_platform_no_input(self):
        print('Test stop platform | (Put) ')
        data = {}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_stop_platform(self):
        print('Test stop platform | (Put) all fields ')
        data = {"command" : "stop",
	            "platform_ID" : 58585,
	            "subplatforms_IDS" : [52994, 53033]}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("Success", r.text)

    def test_stop_platform_wrong_fields(self):
        print('Test stop platform | (Put) wrong fields ')
        data = {"command" : "stop",
	            "platform_ID" : 585,
	            "subplatforms_IDS" : [524, 53]}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)

    def test_stop_platform_missing_fields(self):
        print('Test stop platform | (Put) missing fields ')
        data = {"command" : "stop",
	            "platform_ID" : 58585}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)

    def test_platform_inexistent_command(self):
        print('Test platform | (Put) inexistent command ')
        data = {"command" : "srt",
	            "platform_ID" : 585,
	            "subplatforms_IDS" : [524, 53]}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)

    def test_request_handler_no_input(self):
        print('Test request handler platform | (Put) no input')
        data = {}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_request_handler(self):
        print('Test request handler platform | (Put) all fields')
        data = {"command" : "configure",
	            "platform_ID" : 44224,
	            "subplatforms_IDS" : [14373, 11128],
	            "configuration" : {}}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("Success", r.text)

    def test_request_handler_wrong_fields(self):
        print('Test request handler platform | (Put) wrong fields')
        data = {"command" : "configure",
	            "platform_ID" : 44,
	            "subplatforms_IDS" : [14373, 11128],
	            "configuration" : {}}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)

    def test_request_handler_missing_fields(self):
        print('Test request handler platform | (Put) missing fields')
        data = {"command" : "configure",
	            "platform_ID" : 44224}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)

    def test_alias_no_input(self):
        print('Test alias | (Put) no input')
        data = {}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_alias(self):
        print('Test alias | (Put) all fields')
        data = {"alias" : "testing",
	            "platform_ID" : 44224}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_alias_wrong_fields(self):
        print('Test alias | (Put) wrong fields')
        data = {"alias" : "testing",
	            "platform_ID" : 4}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)

    def test_alias_missing_fields(self):
        print('Test alias | (Put) missing fields')
        data = {"alias" : "testing"}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)

    def test_note_no_input(self):
        print('Test note | (Put) no input')
        data = {}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_note(self):
        print('Test note | (Put) all fields')
        data = {"note" : "testing",
	            "platform_ID" : 44224}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("true", r.text)

    def test_note_wrong_fields(self):
        print('Test note | (Put) wrong fields')
        data = {"note" : "testing",
	            "platform_ID" : 4}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("false", r.text)

    def test_note_missing_fields(self):
        print('Test note | (Put) missing fields')
        data = {"note" : "testing"}
        r = requests.put(users_url, json=data)
        print(r.text)
        self.assertIn("Missing data for required field", r.text)

    def test_delete_platform_no_input(self):
        print('Test platform | (Delete) ')
        data = {}
        r = requests.delete(users_url, json=data)
        print(r.text)
        self.assertIn("No input data provided", r.text)

    def test_delete_platform(self):
        print('Test platform | (Delete) ')
        data = {"platform_ID" : 44224,
	            "subplatforms" : [14373, 11128]}
        r = requests.delete(users_url, json=data)
        print(r.text)
        self.assertIn("Success", r.text)

    def test_delete_platform_wrong_fields(self):
        print('Test platform | (Delete) wrong fields')
        data = {"platform_ID" : 4,
	            "subplatforms" : [14373, 11128]}
        r = requests.delete(users_url, json=data)
        print(r.text)
        self.assertIn("a", r.text)

    def test_delete_platform_missing_fields(self):
        print('Test platform | (Delete) ')
        data = {"platform_ID" : 58585}
        r = requests.delete(users_url, json=data)
        print(r.text)
        self.assertIn("Internal Server Error", r.text)


if __name__ == '__main__':
    print ("TEST - Platform API")
    unittest.main()