# Connection Related Requests #
from flask import request
from flask_restful import Resource

from Schemas.Connection_Schema import *


class ConnectionAPI(Resource):
    from ConnectionManager.ConnectionManager import ConnectionManager
    ConnectionManager = ConnectionManager()

    # To do a get request
    # Type 1
    # {
    #     session_list : Boolean
    # }
    @staticmethod
    def get(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_get_request_schema.load(json_data)
        if errors:
            return errors, 422
        results = ""
        if data["session_list"]:
            results = self.ConnectionManager.update_session_list()
            results = {"usersDictionary": results}
            results, errors = connection_post_response_schema.validate(results)
            if errors:
                return {"success": False}, 503
        return results

    # To do a post request
    # Type 1
    # {
    #     usernames : List[String]
    # }
    # Type 2
    # {
    #     num_users : Integer
    # }
    @staticmethod
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_post_request_schema.load(json_data)
        if errors:
            return errors, 422

        results = ""
        if "usernames" in data:
            results = self.ConnectionManager.fileAddUsers(data["usernames"])
        elif "num_users" in data:
            results = self.ConnectionManager.addUsers(data["num_users"])

        results = {"usersDictionary": results}
        results, errors = connection_post_response_schema.validate(results)

        if errors:
            return {"success": False}, 503

        return results

    # To do a delete request
    # Type 1
    # {
    #     "list_of_users" : List[String]
    # }
    @staticmethod
    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_delete_request_schema.load(json_data)
        if errors:
            return errors, 422

        results = self.ConnectionManager.deleteUsers(data["list_of_users"])

        if results:
            return {"success": True}
        else:
            return {"success": False}, 503

    # To do a put request:
    # Type 1
    # {
    #     "command" : "start" To start polling thread
    # }
    # Type 2
    # {
    #     "command" : "stop" To stop polling thread
    # }
    # Type 3
    # {
    #     "currUsername" : String
    #     "newUsername" : String
    #     "newPassword" : String
    #     "newIP" : String
    # }
    @staticmethod
    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_post_request_schema.load(json_data)
        if errors:
            return errors, 422

        if "command" in data:
            results = True
            if data["command"] == "start":
                self.ConnectionManager.pptp_poll_connection()
            elif data["command"] == "stop":
                self.ConnectionManager.stop()
            else:
                results = False
        else:
            results = self.ConnectionManager.updateUserConnection(data["currUsername"], data["newUsername"],
                                                                  data["newPassword"], data["newIP"])
        if results:
            return {"success": True}
        else:
            return {"success": False}, 503
