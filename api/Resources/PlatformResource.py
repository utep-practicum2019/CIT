# Platform Related Requests #
from flask import request
from flask_restful import Resource

from CIT_API_Schema import *


class PlatformAPI(Resource):

    def get(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        errors = platform_get_request_schema.validate(json_data)
        if errors:
            return errors, 422
        from PlatformManager.PlatformInterface import PlatformInterface
        results = PlatformInterface.get(json_data)
        print(results)
        results, errors = platform_get_response_schema.dump(results)
        print(results)
        return results

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        errors = platform_post_request_schema.validate(json_data)
        if errors:
            return errors, 422
        from PlatformManager.PlatformInterface import PlatformInterface
        results = PlatformInterface.post(json_data)
        results = platform_post_response_schema.dump(results)
        return results

    # def put(self):
    #     json_data = request.get_json(force=True)
    #     if not json_data:
    #         return {'message': 'No input data provided'}, 400
    #     data, errors = platform_request_schema.load(json_data)
    #     if errors:
    #         return errors, 422
    #     # results = PlatformManager.modifyPlatform(data)
    #     results = {
    #         'success': True
    #     }
    #     results = platform_response_schema.dump(results)
    #     return results
    #
    # def delete(self):
    #
    #     json_data = request.get_json(force=True)
    #     if not json_data:
    #         return {'message': 'No input data provided'}, 400
    #     data, errors = platform_request_schema.load(json_data)
    #     if errors:
    #         return errors, 422
    #     # results = PlatformManager.deletePlatform(data[platform_id])
    #     results = {
    #         'success': True
    #     }
    #     results = platform_response_schema.dump(results)
    #     return results
