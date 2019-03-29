# Platform Related Requests #
from flask import request
from flask_restful import Resource

from Schemas.Rocket_Chat_Schema import *


class RocketChatAPI(Resource):
    from .PlatformManagerInstance import PlatformManagerInstance
    platform_interface = PlatformManagerInstance.getInstance().platform_interface

    # rocketChatRegisterUser(self, platform_ID, subplatforms_IDS, user_email, username, user_pass, user_nick)
    # rocketChatCreateChannel(self, platform_ID, subplatforms_IDS, channel_name)
    # rocketChatCreatePrivateGroup(self, platform_ID, subplatforms_IDS, group_name)
    # rocketChatCreateUserToken(self, platform_ID, subplatforms_IDS, user_ID, username)
    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = rocketchat_user_post_request_schema.load(json_data)
        if errors:
            return errors, 422

        if "channel_name" in data:
            results = RocketChatAPI.platform_interface.rocketChatCreateChannel(data["platform_ID"],
                                                                               data["subplatforms_IDS"],
                                                                               data["channel_name"])
        elif "group_name" in data:
            results = RocketChatAPI.platform_interface.rocketChatCreatePrivateGroup(data["platform_ID"],
                                                                                    data["subplatforms_IDS"],
                                                                                    data["group_name"])
        elif "user_ID" in data:
            results = RocketChatAPI.platform_interface.rocketChatCreateUserToken(data["platform_ID"],
                                                                                 data["subplatforms_IDS"],
                                                                                 data["user_ID"], data["username"])
        else:
            results = RocketChatAPI.platform_interface.rocketChatRegisterUser(data["platform_ID"],
                                                                              data["subplatforms_IDS"],
                                                                              data["user_email"], data["username"],
                                                                              data["user_pass"],
                                                                              data["user_nick"])
        if results is None:
            results = {"success": False}
        return results

    # rocketChatLoginUser(self, platform_ID, subplatforms_IDS, username, user_pass)
    # rocketChatPostNewMessage(self, platform_ID, subplatforms_IDS, room_ID, announcement)
    @staticmethod
    def put():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = rocketchat_user_login_request_schema.load(json_data)
        if errors:
            return errors, 422

        if "announcement" in data and "room_ID" in data:
            results = RocketChatAPI.platform_interface.rocketChatPostNewMessage(data["platform_ID"],
                                                                                data["subplatforms_IDS"],
                                                                                data["room_ID"],
                                                                                data["announcement"])
        else:
            results = RocketChatAPI.platform_interface.rocketChatLoginUser(data["platform_ID"],
                                                                           data["subplatforms_IDS"],
                                                                           data["username"],
                                                                           data["user_pass"])
        if results is None:
            results = {"success": False}
        return results

    # rocketChatGetUserInfo(self, platform_ID, subplatforms_IDS, user_ID, username)
    @staticmethod
    def get():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = rocketchat_user_get_request_schema.load(json_data)
        if errors:
            return errors, 422
        results = RocketChatAPI.platform_interface.rocketChatGetUserInfo(data["platform_ID"], data["subplatforms_IDS"],
                                                                         data["user_ID"], data["username"])
        if results is None:
            results = {"success": False}
        return results

    # rocketChatDeleteUser(self, platform_ID, subplatforms_IDS, user_ID)
    # rocketChatDeleteChannel(self, platform_ID, subplatforms_IDS, channel_ID)
    # rocketChatDeletePrivateGroup(self, platform_ID, subplatforms_IDS, room_ID)
    @staticmethod
    def delete():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = rocketchat_user_delete_request_schema.load(json_data)
        if errors:
            return errors, 422

        if "channel_ID" in data:
            results = RocketChatAPI.platform_interface.rocketChatDeleteChannel(data["platform_ID"],
                                                                               data["subplatforms_IDS"],
                                                                               data["channel_ID"])
        elif "room_ID" in data:
            results = RocketChatAPI.platform_interface.rocketChatDeletePrivateGroup(data["platform_ID"],
                                                                                    data["subplatforms_IDS"],
                                                                                    data["room_ID"])
        else:
            results = RocketChatAPI.platform_interface.rocketChatGetUserInfo(data["platform_ID"],
                                                                             data["subplatforms_IDS"],
                                                                             data["user_ID"])
        if results is None:
            results = {"success": False}
        return results
