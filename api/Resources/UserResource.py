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
        json_data = request.args.to_dict()
        # if not json_data:
        #     return {'message': 'No input data provided'}, 400
        data, errors = user_get_request_schema.load(json_data)
        if errors:
            return errors, 422
        from Database.database_handler import DatabaseHandler
        if "username" in data:
            results = DatabaseHandler.find('users', data["username"])
            if results is None or not results:
                return {"success": False}, 404
            return user_schema.dump(User(**results))
        else:
            results = DatabaseHandler.find_all('users')
            formatted_results = []
            for result in results:
                group = result['group_id']
                group_object = DatabaseHandler.find("groups", group)
                try:
                    alias = group_object["alias"]
                except TypeError:
                    alias = ''
                if alias is not None and alias != "":
                    formatted_group = " " + alias + " (" + str(group) + ")"
                else:
                    formatted_group = " " + str(group)
                r = user_schema.dump(User(**result))
                r[0]['group_id'] = formatted_group
                formatted_results.append(r[0])
            return formatted_results


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
