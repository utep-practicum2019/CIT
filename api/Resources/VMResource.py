from flask import request
from flask_restful import Resource

import inputValidator as inputValidator
from CITAPI_Schema import *


class VMConfigAPI(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = vm_config_schema.load(json_data)

        if errors:
            return errors, 422

        command = ""
        if 'vmName' in data:
            command += "vmname " + data['vmName'] + " "
        if 'src_ip' in data:
            if inputValidator.is_valid_ipv4_address(data['src_ip']):
                command += "src_ip " + data['src_ip'] + " "
            else:
                return {'message': 'Not a valid IP address'}, 400
        if 'src_prt' in data:
            command += "src_prt" + data['src_prt'] + " "
        if 'dst_ip' in data:
            if inputValidator.is_valid_ipv4_address(data['src_ip']):
                command += "dst_ip " + data['dst_ip'] + " "
            else:
                return {'message': 'Not a valid IP address'}, 400
        if 'dst_prt' in data:
            command += "dst_prt " + data['dst_prt'] + " "
        if 'adpt_number' in data:
            command += "adpt_number " + data['adpt_number'] + " "

        results = ({'config': command})
        return results


class VMStatusAPI(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = vm_status_schema.load(json_data)

        if errors:
            return errors, 422

        command = ""
        if 'vmName' in data:
            command += "vmname " + data['vmName'] + " "
        if 'mgrStatus' in data:
            command += "mgrstatus " + data['mgrStatus']
        results = ({'status': command})
        return results


class VMStartAPI(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = vm_start_schema.load(json_data)

        if errors:
            return errors, 422

        command = ""
        if 'vmName' in data:
            command += "vmname " + data['vmName']
        results = ({'start': command})
        return results


class VMSuspendAPI(Resource):

    def post(self):
        """VMSuspend view
        ---
        description: Suspend a VM
        responses:
        200:
        content:
            application/json:
            schema: VMSuspendSchema
        """
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        print(json_data)
        data, errors = vm_suspend_schema.load(json_data)

        if errors:
            return errors, 422

        command = ""
        if 'vmName' in data:
            command += "vmname " + data['vmName']
        results = ({'suspend': command})
        return results
