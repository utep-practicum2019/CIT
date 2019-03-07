from flask import Flask, request, make_response, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

import inputValidator as inputValidator
from CITAPI_Schema import *

ma = Marshmallow()
app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'root':
        return 'toor'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


class LoginAPI(Resource):
    decorators = [auth.login_required]

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = login_schema.load(json_data)

        if errors:
            return errors, 422
        if not inputValidator.is_valid_ipv4_address(data['ip']):
            return {'message': 'Not a valid IP address'}, 400
        return "Authenticated User, Assigned " + data['ip'] + " Redirect To: "


class VMConfigAPI(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = vm_config_schema.load(json_data)

        if errors:
            return errors, 422

        command = ""
        if 'vmName' in data:
            command += "vmname " + data['vmName'] + " "
        if 'src_ip' in data:
            if inputValidator.is_valid_ipv4_address(data['src_ip']):
                command += "src_ip " + data['src_ip'] + " "
            else:
                return {'message': 'Not a valid IP address'}, 400
        if 'src_prt' in data:
            command += "src_prt" + data['src_prt'] + " "
        if 'dst_ip' in data:
            if inputValidator.is_valid_ipv4_address(data['src_ip']):
                command += "dst_ip " + data['dst_ip'] + " "
            else:
                return {'message': 'Not a valid IP address'}, 400
        if 'dst_prt' in data:
            command += "dst_prt " + data['dst_prt'] + " "
        if 'adpt_number' in data:
            command += "adpt_number " + data['adpt_number'] + " "

        results = ({'config': command})
        return results


class VMStatusAPI(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = vm_status_schema.load(json_data)

        if errors:
            return errors, 422

        command = ""
        if 'vmName' in data:
            command += "vmname " + data['vmName'] + " "
        if 'mgrStatus' in data:
            command += "mgrstatus " + data['mgrStatus']
        results = ({'status': command})
        return results


class VMStartAPI(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = vm_start_schema.load(json_data)

        if errors:
            return errors, 422

        command = ""
        if 'vmName' in data:
            command += "vmname " + data['vmName']
        results = ({'start': command})
        return results


class VMSuspendAPI(Resource):

    def post(self):
        """VMSuspend view
        ---
        description: Suspend a VM
        responses:
        200:
        content:
            application/json:
            schema: VMSuspendSchema
        """

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        print(json_data)
        data, errors = vm_suspend_schema.load(json_data)

        if errors:
            return errors, 422

        command = ""
        if 'vmName' in data:
            command += "vmname " + data['vmName']
        results = ({'suspend': command})
        return results


# User Related Requests #


class UserAPI(Resource):

    def get(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = user_request_schema.load(json_data)
        if errors:
            return errors, 422
        from AccountManager.account_manager import AccountManager
        results = AccountManager.get_user(data["username"])
        if not results:
            return "User Not Found", 404
        results = user_schema.dump(results)
        return results

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = user_create_request_schema.load(json_data)
        if errors:
            return errors, 422
        from AccountManager.account_manager import AccountManager
        if "filepath" in data:
            results = AccountManager.create_groups(data["group_count"], data["users_per_group"], data["filepath"])
        else:
            results = AccountManager.create_groups(data["group_count"], data["users_per_group"])

        if results:
            return user_response_schema.dump({"success": results})
        else:
            return "User Already Exists", 409

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = user_update_request_schema.load(json_data)

        if errors:
            return errors, 422

        username = data["username"]
        updated_user = data["updated_user"]
        User.to_json(updated_user)

        from AccountManager.account_manager import AccountManager
        results = AccountManager.update_user(username, updated_user)
        if results:
            return user_response_schema.dump({"success": results})
        else:
            return "User Not Found", 404

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = user_request_schema.load(json_data)

        if errors:
            return errors, 422

        from AccountManager.account_manager import AccountManager
        results = AccountManager.delete_user(data['username'])
        if results:
            return user_response_schema.dump({"success": results})
        else:
            return "User Not Found", 404


# Group Related Requests #

class GroupAPI(Resource):

    def get(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = group_request_schema.load(json_data)

        if errors:
            return errors, 422

        # results = getGroupData(data)
        results = {
            'group_id': 0,
            'min': 0,
            'max': 0,
            'platforms': ['P1', 'P2'],
            'members': ['M1', 'M2'],
            'chat_id': 0,
        }

        results = group_response_schema.dump(results)
        return results

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = group_request_schema.load(json_data)

        if errors:
            return errors, 422

        group_id = data["group_id"]
        del data["group_id"]

        from AccountManager.account_manager import AccountManager
        results = AccountManager.create_group(group_id, **data)

        results = group_response_schema.dump(results)
        results = {"success": results}

        return results

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = group_update_request_schema.load(json_data)

        if errors:
            return errors, 422

        group_id = data["group_id"]
        updated_group = data["updated_group"]

        from AccountManager.account_manager import AccountManager
        results = AccountManager.update_group(group_id, updated_group)

        results = group_response_schema.dump(results)
        return results

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = group_request_schema.load(json_data)

        if errors:
            return errors, 422

        group_id = data["group_id"]

        from AccountManager.account_manager import AccountManager
        results = AccountManager.delete_group(group_id)
        results = group_response_schema.dump(results)

        return results


# Platform Related Requests #

class PlatformAPI(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = platform_create_request_schema.load(json_data)

        if errors:
            return errors, 422
        # results = PlatformManager.addPlatform(data)
        results = {
            'success': True
        }
        results = platform_response_schema.dump(results)
        return results

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = platform_request_schema.load(json_data)
        if errors:
            return errors, 422
        # results = PlatformManager.modifyPlatform(data)
        results = {
            'success': True
        }
        results = platform_response_schema.dump(results)
        return results

    def delete(self):

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = platform_request_schema.load(json_data)
        if errors:
            return errors, 422
        # results = PlatformManager.deletePlatform(data[platform_id])
        results = {
            'success': True
        }
        results = platform_response_schema.dump(results)
        return results


# Connection Related Requests #

class ConnectionAPI(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_request_schema.load(json_data)
        if errors:
            return errors, 422
        if 'num_users' in data:
            # results = createUserConnection(data['num_users'])
            results = {
                'success': True
            }
            results = group_response_schema.dump(results)
            return results
        else:
            return {'message': "An appropriate parameter is missing from the request"}, 422

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_request_schema.load(json_data)
        if errors:
            return errors, 422
        if 'list_of_users' in data:
            # results = deleteUserConnection(data['list_of_users'])
            results = {
                'success': True
            }
            results = group_response_schema.dump(results)
            return results
        else:
            return {'message': "An appropriate parameter is missing from the request"}, 422

    def put(self):

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_request_schema.load(json_data)
        if errors:
            return errors, 422
        if 'username' and 'password' in data:
            # results = updateUserConnection(data['username'], data['password'])
            results = {
                'success': True
            }
            results = group_response_schema.dump(results)
            return results
        else:
            return {'message': "An appropriate parameter is missing from the request"}, 422


# Database Related Requests #

class DatabaseAPI(Resource):

    def get(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        from Database.database_handler import DatabaseHandler
        results = DatabaseHandler.find(json_data["collection_name"], json_data["document_id"])
        if results is None:
            return "Not Found", 404
        return results

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        from Database.database_handler import DatabaseHandler
        collection_name = json_data["collection_name"]
        document_id = json_data["document_id"]
        document = json_data["document"]
        results = DatabaseHandler.insert(collection_name, document_id, document)
        if results:
            return user_response_schema.dump({"success": results})
        else:
            return "Document Already Exists", 409

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = database_modify_schema.load(json_data)
        if errors:
            return errors, 422
        from Database.database_handler import DatabaseHandler
        collection_name = json_data["collection_name"]
        document_id = json_data["document_id"]
        document = json_data["document"]
        results = DatabaseHandler.update(collection_name, document_id, document)
        if results:
            return user_response_schema.dump({"success": results})
        else:
            return "Document Not Found", 404

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        from Database.database_handler import DatabaseHandler
        collection_name = json_data["collection_name"]
        document_id = json_data["document_id"]
        results = DatabaseHandler.delete(collection_name, document_id)
        if results:
            return user_response_schema.dump({"success": results})
        else:
            return "Document Not Found", 404


api.add_resource(DatabaseAPI, '/api/v2/resources/database')
api.add_resource(ConnectionAPI, '/api/v2/resources/connection')
api.add_resource(UserAPI, '/api/v2/resources/user')
api.add_resource(GroupAPI, '/api/v2/resources/group')
api.add_resource(PlatformAPI, '/api/v2/resources/platform')
api.add_resource(VMConfigAPI, '/api/v2/resources/vm/manage/config')
api.add_resource(VMStatusAPI, '/api/v2/resources/vm/manage/status')
api.add_resource(VMStartAPI, '/api/v2/resources/vm/manage/start')
api.add_resource(VMSuspendAPI, '/api/v2/resources/vm/manage/suspend')
api.add_resource(LoginAPI, '/api/v2/resources/login')

if __name__ == '__main__':
    app.run()
