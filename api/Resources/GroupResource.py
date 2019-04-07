# Group Related Requests #
from flask import request
from flask_restful import Resource

from Schemas.Group_Schema import *
from Schemas.User_Schema import *


class GroupAPI(Resource):

    # To do a get request
    # Type 1
    # {
    #     group_id : Integer
    # }
    @staticmethod
    def get():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = group_get_request_schema.load(json_data)
        if errors:
            return errors, 422

        from Database.database_handler import DatabaseHandler
        results = DatabaseHandler.find('groups', data["group_id"])
        if results is None or not results:
            return {"success": False}, 404
        return group_schema.dump(Group(**results))

    # To do a post request
    # Type 1
    # {
    #     group_count : Integer
    #     users_per_group : Integer
    #     filepath : String (Optional)
    # }
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
            return group_response_schema.dump({"success": results})
        else:
            return {"success": False}, 409

    # To do a put request
    # Type 1
    # {
    #     group_id : Integer
    #     updated_group : Group
    # }
    @staticmethod
    def put():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = group_update_request_schema.load(json_data)

        if errors:
            return errors, 422
        from AccountManager.account_manager import AccountManager

        results = False
        if "command" in data and "platform_id" in data:
            if data["command"] == "attach":
                results = AccountManager.attach_platform(data["group_id"], data["platform_id"])
            elif data["command"] == "detach":
                results = AccountManager.detach_platform(data["platform_id"])
        else:
            results = AccountManager.update_group(data["group_id"], data["updated_group"])

        if results:
            return group_response_schema.dump({"success": results})
        else:
            return {"success": False}, 409

    # To do a delete request
    # Type 1
    # {
    #     group_id : Integer
    # }
    @staticmethod
    def delete():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = group_delete_request_schema.load(json_data)

        if errors:
            return errors, 422

        from AccountManager.account_manager import AccountManager
        errors = []
        for group in data['list_of_groups']:
            try:
                AccountManager.delete_group(group)
            except ValueError as e:
                errors.append("Error deleting group " + group + ": " + str(e))
        if errors:
            print(errors)
            return {"success": False, "errors": errors}, 200

        return {"success": True}, 200
