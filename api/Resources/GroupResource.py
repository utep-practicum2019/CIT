# Group Related Requests #
from flask import request
from flask_restful import Resource

from CITAPI_Schema import *


class GroupAPI(Resource):

    def get(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = group_request_schema.load(json_data)

        if errors:
            return errors, 422

        # results = getGroupData(data)
        results = {
            'group_id': 0,
            'min': 0,
            'max': 0,
            'platforms': ['P1', 'P2'],
            'members': ['M1', 'M2'],
            'chat_id': 0,
        }

        results = group_response_schema.dump(results)
        return results

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = group_request_schema.load(json_data)

        if errors:
            return errors, 422

        group_id = data["group_id"]
        del data["group_id"]

        from AccountManager.account_manager import AccountManager
        results = AccountManager.create_group(group_id, **data)

        results = group_response_schema.dump(results)
        results = {"success": results}

        return results

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = group_update_request_schema.load(json_data)

        if errors:
            return errors, 422

        group_id = data["group_id"]
        updated_group = data["updated_group"]

        from AccountManager.account_manager import AccountManager
        results = AccountManager.update_group(group_id, updated_group)

        results = group_response_schema.dump(results)
        return results

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = group_request_schema.load(json_data)

        if errors:
            return errors, 422

        group_id = data["group_id"]

        from AccountManager.account_manager import AccountManager
        results = AccountManager.delete_group(group_id)
        results = group_response_schema.dump(results)

        return results
