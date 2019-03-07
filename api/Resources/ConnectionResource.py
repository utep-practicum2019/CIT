# Connection Related Requests #
from flask import request
from flask_restful import Resource

from CITAPI_Schema import *


class ConnectionAPI(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_request_schema.load(json_data)
        if errors:
            return errors, 422
        if 'num_users' in data:
            # results = createUserConnection(data['num_users'])
            results = {
                'success': True
            }
            results = group_response_schema.dump(results)
            return results
        else:
            return {'message': "An appropriate parameter is missing from the request"}, 422

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_request_schema.load(json_data)
        if errors:
            return errors, 422
        if 'list_of_users' in data:
            # results = deleteUserConnection(data['list_of_users'])
            results = {
                'success': True
            }
            results = group_response_schema.dump(results)
            return results
        else:
            return {'message': "An appropriate parameter is missing from the request"}, 422

    def put(self):

        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_request_schema.load(json_data)
        if errors:
            return errors, 422
        if 'username' and 'password' in data:
            # results = updateUserConnection(data['username'], data['password'])
            results = {
                'success': True
            }
            results = group_response_schema.dump(results)
            return results
        else:
            return {'message': "An appropriate parameter is missing from the request"}, 422
