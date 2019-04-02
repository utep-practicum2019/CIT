# User Related Requests #
from flask import request
from flask_restful import Resource

from Schemas.User_Schema import *


class UserAPI(Resource):

    # To do a get request
    # Type 1
    # {
    #     username : String
    # }
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
            return {"success": False}, 404
        return user_schema.dump(User(**results))

    # To do a put request
    # Type 1
    # {
    #     username : String
    #     updated_user : User
    # }
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

        from AccountManager.account_manager import AccountManager
        results = AccountManager.update_user(username, updated_user)
        if results:
            return user_response_schema.dump({"success": results})
        else:
            return {"success": results}, 404

    # To do a delete request
    # Type 1
    # {
    #     list_of_users : List[String]
    # }
    @staticmethod
    def delete():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = user_delete_request_schema.load(json_data)

        if errors:
            return errors, 422

        from AccountManager.account_manager import AccountManager

        errors = []
        for user in data['list_of_users']:
            # try:
            #     AccountManager.delete_user(user)
            # except ValueError as e:
            #     errors.append("Error deleting user " + user + ": " + str(e))
            AccountManager.delete_user(user)
        if errors:
            print(errors)
            return {"success": False, "errors" : errors}, 200

        return {"success": True}, 200
