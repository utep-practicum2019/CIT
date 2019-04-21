# Group Related Requests #
import re
from flask import request
from flask_restful import Resource

from Schemas.Group_Schema import *
from Schemas.User_Schema import *
from Database.database_handler import DatabaseHandler
from Resources.PlatformManagerInstance import PlatformManagerInstance


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
                r = group_schema.dump(Group(**result))

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
                    if not results:
                        print("Failed to attach {} to group {}".format(plat, data["group_id"]))
                        continue

                    plat_info = DatabaseHandler.find('platforms', plat)
                    for current in plat_info['subplatforms']:
                        if 'Rocketchat' == current['name']:
                            platform_man = PlatformManagerInstance.get_instance()
                            # running = platform_man.getPlatformStatus(plat_info['main']['id'], current['id'])
                            running = True
                            if not running:
                                platform_man.platform_interface.startPlatform(plat_info['main']['id'], current['id'])

                            group_info = DatabaseHandler.find('groups', data["group_id"])
                            command = {
                                'command': 'registerUser',
                                'param': {}
                            }
                            for user in group_info['members']:
                                command['param']['username'] = user
                                command['param']['email'] = user + "@citsystem.com"
                                user_info = DatabaseHandler.find('users', user)
                                command['param']['password'] = user_info['password']
                                success, user_id = platform_man.platform_interface.requestHandler(plat_info['main']['id'], current['id'], command)

                            if not running:
                                platform_man.platform_interface.stopPlatform(plat_info['main']['id'], current['id'])
                            break

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
