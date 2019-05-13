# Platform Related Requests #
from flask import request
from flask_restful import Resource

from AccountManager.account_manager import AccountManager
from Database.database_handler import DatabaseHandler
from Schemas.Platform_Schema import *


def format_status(platform):
    results = "Stopped"
    if len(platform["subplatforms"]) == 0:
        if PlatformAPI.platform_interface.getPlatformStatus(platform["main"]["id"]):
            results = "Running"
    elif len(platform["subplatforms"]) == 1:
        if PlatformAPI.platform_interface.getPlatformStatus(platform["main"]["id"]):
            results = "Running"
    else:
        at_least_one = 0
        for plat in platform["subplatforms"]:
            if PlatformAPI.platform_interface.getPlatformStatus(platform["main"]["id"], plat["id"]):
                at_least_one += 1
        results = str(at_least_one) + " Running"
    return results


class PlatformAPI(Resource):
    from .PlatformManagerInstance import PlatformManagerInstance
    platform_interface = PlatformManagerInstance.get_instance().platform_interface
    from Resources import AuthResource

    @staticmethod
    @AuthResource.is_admin_only
    def get():

        json_data = request.args.to_dict()
        print("GET PLATFORMS: " + str(json_data))
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = platform_get_request_schema.load(json_data)
        if errors:
            return errors, 422
        results = {"success": False}

        if "all" in data:
            if data["all"]:
                # from Database.database_handler import DatabaseHandler
                # results = DatabaseHandler.find_all("platforms")
                # for plat in results:
                #     plat["status"] = format_status(plat)
                # return results
                from Database.database_handler import DatabaseHandler
                return DatabaseHandler.find_all("platforms")
            else:
                results = PlatformAPI.platform_interface.getAvailablePlugins()
                if results is None:
                    results = {"success": False}
        elif "status" in data:
            if "sub" in data:
                from Database.database_handler import DatabaseHandler
                results = DatabaseHandler.find("platforms", data["platform_ID"])
                for plat in results["subplatforms"]:
                    plat["status"] = PlatformAPI.platform_interface.getPlatformStatus(data["platform_ID"], plat["id"])
            else:
                from Database.database_handler import DatabaseHandler
                results = DatabaseHandler.find("platforms", data["platform_ID"])
                results = format_status(results)
                # if len(results["subplatforms"]) == 0:
                #     results = PlatformAPI.platform_interface.getPlatformStatus(data["platform_ID"])
                # elif len(results["subplatforms"]) == 1:
                #     results = PlatformAPI.platform_interface.getPlatformStatus(data["platform_ID"])
                # else:
                #     at_least_one = False
                #     for plat in results["subplatforms"]:
                #         at_least_one = at_least_one or PlatformAPI.platform_interface.getPlatformStatus(
                #             data["platform_ID"], plat["id"])
                #     results = at_least_one
        elif "alias" in data:
            from Database.database_handler import DatabaseHandler
            results = DatabaseHandler.find("platforms", data["platform_ID"])
            if results:
                results = results["main"]["alias"]
        return results

    @staticmethod
    @AuthResource.is_admin_only
    def post():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = platform_post_request_schema.load(json_data)
        if errors:
            return errors, 422
        results = PlatformAPI.platform_interface.createPlatform(data["main_platform"], data["subplatforms"])
        if results is None:
            results = {"success": False}
        return results

    @staticmethod
    @AuthResource.is_admin_only
    def put():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        if "command" in json_data:
            data, errors = platform_command_request_schema.load(json_data)
            if errors:
                return errors, 422
            if json_data["command"] == "start":
                results = PlatformAPI.platform_interface.startPlatform(data["platform_ID"], data["subplatforms_IDS"])

            elif json_data["command"] == "stop":
                results = PlatformAPI.platform_interface.stopPlatform(data["platform_ID"], data["subplatforms_IDS"])

            elif json_data["command"] == "configure":
                results = PlatformAPI.platform_interface.requestHandler(data["platform_ID"],
                                                                        data["subplatforms_IDS"][0],
                                                                        data["configuration"])
            else:
                results = {"success": False}
        else:
            data, errors = platform_put_request_schema.load(json_data)
            if errors:
                return errors, 422
            if "note" in data:
                note = data["note"]
                main_id = data["platform_ID"]
                results = PlatformAPI.platform_interface.editPlatformNote(main_id, note)
            elif "alias" in data:
                alias = data["alias"]
                main_id = data["platform_ID"]
                results = PlatformAPI.platform_interface.editPlatformAlias(main_id, alias)
            else:
                results = PlatformAPI.platform_interface.addPlatform(data["platform_ID"], data["subplatforms"])
        if results is None:
            results = {"success": False}
        return results

    @staticmethod
    @AuthResource.is_admin_only
    def delete():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = platform_delete_request_schema.load(json_data)
        if errors:
            return errors, 422
        results = PlatformAPI.platform_interface.deletePlatform(data["platform_ID"], data["subplatforms_IDS"])
        if results == 'Success':
            group = DatabaseHandler.groupCheck(data["platform_ID"])
            while group is not None:
                AccountManager.detach_platform(group['group_id'], data["platform_ID"])
                group = DatabaseHandler.groupCheck(data["platform_ID"])
        if results is None:
            results = {"success": False}
        return results
