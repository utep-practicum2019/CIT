from flask import request, make_response, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource
from Schemas.Login_Schema import *

import inputValidator as inputValidator


auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'root':
        return 'toor'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


class LoginAPI(Resource):
    decorators = [auth.login_required]

    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = login_schema.load(json_data)

        if errors:
            return errors, 422
        if not inputValidator.is_valid_ipv4_address(data['ip']):
            return {'message': 'Not a valid IP address'}, 400
        return "Authenticated User, Assigned " + data['ip'] + " Redirect To: "
