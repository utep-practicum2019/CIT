# User Related Requests #
from flask import request
from flask_restful import Resource

from CIT_API_Schema import *


class UserAPI(Resource):

    @staticmethod
    def get():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = user_request_schema.load(json_data)
        if errors:
            return errors, 422

        from Database.database_handler import DatabaseHandler
        results = DatabaseHandler.find('users', data["username"])
        if results is None or not results:
            results = user_response_schema.dump({"success": False})
            return {"success": False}, 404
        return user_schema.dump(User(**results))

    @staticmethod
    def post():
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
            return {"success": results}, 409

    @staticmethod
    def put():
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
            return {"success": results}, 404

    @staticmethod
    def delete():
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
            return {"success": results}, 404
