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
        json_data = request.args.to_dict()
        # if not json_data:
        #     return {'message': 'No input data provided'}, 400
        data, errors = group_get_request_schema.load(json_data)
        if errors:
            return errors, 422
        from Database.database_handler import DatabaseHandler
        if "group_id" in data:
            results = DatabaseHandler.find('groups', data["group_id"])
            if results is None or not results:
                return {"success": False}, 404
            return group_schema.dump(Group(**results))
        else:
            results = DatabaseHandler.find_all('groups')
            formatted_results = []
            for result in results:
                if 'platforms' not in result:
                    result['platforms'] = []
                if 'note' not in result:
                    result['note'] = ""
                if 'alias' not in result:
                    result['alias'] = ""
                formatted_platforms = []
                from Database.database_handler import DatabaseHandler
                for platform in result['platforms']:
                    platform_object = DatabaseHandler.find("platforms", platform)
                    if platform_object:
                        alias = platform_object["main"]["alias"]
                        name = platform_object["main"]["name"]
                        formatted_platform = alias + " ID: " + str(platform) + " Type: " + name
                        formatted_platforms.append(formatted_platform)
                formatted_users = []
                for user in result['members']:
                    user_object = DatabaseHandler.find("users", user)
                    alias = user_object["alias"]
                    if alias is not None and alias != "":
                        formatted_user = " " + alias + " (" + user + ")"
                    else:
                        formatted_user = " " + user
                    formatted_users.append(formatted_user)
                r = group_schema.dump(Group(**result))
                r[0]['platforms'] = formatted_platforms
                r[0]['members'] = formatted_users
                formatted_results.append(r[0])

            return formatted_results

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
        if "command" in data and "platform_ids" in data:
            if data["command"] == "attach":
                for plat in data["platform_ids"]:
                    results = AccountManager.attach_platform(data["group_id"], plat)

                # from Database.database import Database
                # group = Database.find("groups", data["group_id"])
                # from .PlatformManagerInstance import PlatformManagerInstance
                # platform_interface = PlatformManagerInstance.get_instance().platform_interface
                # g_name = "Group " + str(data["group_id"])
                # group_data = platform_interface.rocketChatCreatePrivateGroup(data["platform_id"],
                #                                                              "Whatever",
                #                                                              g_name)
                # for user in group["members"]:
                #     email = user["username"] + "@cit.com"
                #     username = user["username"]
                #     password = user["password"]
                #     nickname = user["username"]
                #     u_info = platform_interface.rocketChatRegisterUser(data["platform_id"],
                #                                                        "Whatever",
                #                                                        email, username,
                #                                                        password,
                #                                                        nickname)
                #     platform_interface.addUserGroup(data["platform_id"], group_data["Room_ID"], u_info["User_ID"])

                return True




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
