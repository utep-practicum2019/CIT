# Platform Related Requests #
from flask import request
from flask_restful import Resource

from CIT_API_Schema import *


class PlatformAPI(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = platform_create_request_schema.load(json_data)

        if errors:
            return errors, 422
        # results = PlatformManager.addPlatform(data)
        results = {
            'success': True
        }
        results = platform_response_schema.dump(results)
        return results

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = platform_request_schema.load(json_data)
        if errors:
            return errors, 422
        # results = PlatformManager.modifyPlatform(data)
        results = {
            'success': True
        }
        results = platform_response_schema.dump(results)
        return results

    def delete(self):

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = platform_request_schema.load(json_data)
        if errors:
            return errors, 422
        # results = PlatformManager.deletePlatform(data[platform_id])
        results = {
            'success': True
        }
        results = platform_response_schema.dump(results)
        return results
