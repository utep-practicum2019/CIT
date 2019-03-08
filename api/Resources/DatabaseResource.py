# Database Related Requests #
from flask import request
from flask_restful import Resource

from CIT_API_Schema import *


class DatabaseAPI(Resource):

    def get(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        from Database.database_handler import DatabaseHandler
        results = DatabaseHandler.find(json_data["collection_name"], json_data["document_id"])
        if results is None:
            return {"success": False}, 404
        return results

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        from Database.database_handler import DatabaseHandler
        collection_name = json_data["collection_name"]
        document_id = json_data["document_id"]
        document = json_data["document"]
        results = DatabaseHandler.insert(collection_name, document_id, document)
        if results:
            return user_response_schema.dump({"success": results})
        else:
            return {"success": results}, 409

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = database_modify_schema.load(json_data)
        if errors:
            return errors, 422
        from Database.database_handler import DatabaseHandler
        collection_name = json_data["collection_name"]
        document_id = json_data["document_id"]
        document = json_data["document"]
        results = DatabaseHandler.update(collection_name, document_id, document)
        if results:
            return user_response_schema.dump({"success": results})
        else:
            return {"success": results}, 404

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        from Database.database_handler import DatabaseHandler
        collection_name = json_data["collection_name"]
        document_id = json_data["document_id"]
        results = DatabaseHandler.delete(collection_name, document_id)
        if results:
            return user_response_schema.dump({"success": results})
        else:
            return {"success": results}, 404
