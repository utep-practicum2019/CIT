# Connection Related Requests #
from flask import request
from flask_restful import Resource

from Schemas.Connection_Schema import *


class ConnectionAPI(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_post_request_schema.load(json_data)
        if errors:
            return errors, 422

        from ConnectionManager.ConnectionManager import ConnectionManager
        results = ConnectionManager.addUsers(ConnectionManager(), data["num_users"])
        results = {"usersDictionary": results}
        results, errors = connection_post_response_schema.validate(results)

        if errors:
            return {"success": False}, 503

        return results

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_delete_request_schema.load(json_data)
        if errors:
            return errors, 422

        from ConnectionManager.ConnectionManager import ConnectionManager
        results = ConnectionManager.deleteUsers(ConnectionManager(), data["list_of_users"])

        if results:
            return {"success": True}
        else:
            return {"success": False}, 503

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_post_request_schema.load(json_data)
        if errors:
            return errors, 422

        from ConnectionManager.ConnectionManager import ConnectionManager
        results = ConnectionManager.updateUserConnection(ConnectionManager(), data["currUsername"], data["newUsername"],
                                                         data["newPassword"], data["newIP"])

        if results:
            return {"success": True}
        else:
            return {"success": False}, 503
