# Connection Related Requests #
from flask import request, jsonify
from flask_restful import Resource
from Schemas.Connection_Schema import *
import json

class ConnectionAPI(Resource):
    from ConnectionManager.ConnectionManager import ConnectionManager
    ConnectionManager = ConnectionManager()

    # To do a get request
    # Type 1
    # {
    #     session_list : Boolean
    # }
    @staticmethod
    def get():
        json_data = request.args.to_dict()
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_get_request_schema.load(json_data)
        if errors:
            return errors, 422

        results = ""
        if data["session_list"]:
            results = ConnectionAPI.ConnectionManager.update_session_list()
            results = {"usersDictionary": results}
            # results, errors = connection_post_response_schema.validate(results)
            # if errors:
            #     return {"success": False}, 503
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
    def post():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_post_request_schema.load(json_data)
        if errors:
            return errors, 422

        results = ""
        if "usernames" in data:
            results = ConnectionAPI.ConnectionManager.fileAddUsers(data["usernames"])
        elif "num_users" in data:
            results = ConnectionAPI.ConnectionManager.addUsers(data["num_users"])

        formatted_results = []
        for k in results.keys():
            formatted_results.append(results[k])

        formatted_results = {"usersDictionary": formatted_results}
        errors = connection_post_response_schema.validate(formatted_results)

        if errors:
            print(errors)
            return {"success": False}, 503

        results = {"usersDictionary": results}
        return results

    # To do a delete request
    # Type 1
    # {
    #     "list_of_users" : List[String]
    # }
    @staticmethod
    def delete():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_delete_request_schema.load(json_data)
        if errors:
            return errors, 422

        results = ConnectionAPI.ConnectionManager.deleteUsers(data["list_of_users"])

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
    #     "curr_username" : String
    #     "updated_username" : String
    #     "new_password" : String
    #     "new_ip" : String
    # }
    @staticmethod
    def put():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = connection_put_request_schema.load(json_data)
        if errors:
            return errors, 422
        print(json_data)
        print(data)
        if "command" in data:
            results = True
            if data["command"] == "start":
                ConnectionAPI.ConnectionManager.pptp_poll_connection()
            elif data["command"] == "stop":
                ConnectionAPI.ConnectionManager.stop()
            else:
                results = False
        else:
            results = ConnectionAPI.ConnectionManager.updateUserConnection(data["curr_username"],
                                                                           data["updated_username"],
                                                                           data["new_password"], data["new_ip"])
        if results:
            return {"success": True}
        else:
            return {"success": False}, 503
