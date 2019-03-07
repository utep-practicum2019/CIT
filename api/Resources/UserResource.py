# User Related Requests #
from flask import request
from flask_restful import Resource

from CITAPI_Schema import *


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
