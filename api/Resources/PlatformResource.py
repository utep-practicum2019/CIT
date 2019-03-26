# Platform Related Requests #
from flask import request
from flask_restful import Resource

from Schemas.Platform_Schema import *


class PlatformAPI(Resource):
    import PlatformManager.PlatformInterface as PlatformInterface

    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = platform_post_request_schema.load(json_data)
        if errors:
            return errors, 422
        results = PlatformAPI.PlatformInterface.pi.createPlatform(data["main_platform"], data["subplatforms"])
        if results is None:
            results = {"success": False}
        return results

    @staticmethod
    def put():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        if "command" in json_data:
            data, errors = platform_command_request_schema.load(json_data)
            if errors:
                return errors, 422
            if json_data["command"] == "start":
                results = PlatformAPI.PlatformInterface.pi.startPlatform(data["platform_ID"], data["subplatforms_IDS"])
            elif json_data["command"] == "stop":
                results = PlatformAPI.PlatformInterface.pi.stopPlatform(data["platform_ID"], data["subplatforms_IDS"])
            else:
                results = {"success": False}
        else:
            data, errors = platform_add_request_schema.load(json_data)
            if errors:
                return errors, 422
            results = PlatformAPI.PlatformInterface.pi.addPlatform(data["platform_ID"], data["subplatforms"])
        if results is None:
            results = {"success": False}
        return results

    @staticmethod
    def delete():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = platform_delete_request_schema.load(json_data)
        if errors:
            return errors, 422
        results = PlatformAPI.PlatformInterface.pi.deletePlatform(json_data["main_platform"], json_data["subplatforms"])
        if results is None:
            results = {"success": False}
        return results
