# Platform Related Requests #
from flask import request
from flask_restful import Resource

from Schemas.Rocket_Chat_Schema import *


class RocketChatAPI(Resource):
    import PlatformManager.PlatformInterface as PlatformInterface

    # rocketChatRegisterUser(self, platform_ID, subplatform_ID, user_email, username, user_pass, user_nick)
    # rocketChatCreateChannel(self, platform_ID, subPlatform_ID, channel_name)
    # rocketChatCreatePrivateGroup(self, platform_ID, subPlatform_ID, group_name)
    # rocketChatCreateUserToken(self, platform_ID, subPlatform_ID, user_ID, username)
    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = rocketchat_user_post_request_schema.load(json_data)
        if errors:
            return errors, 422

        if "channel_name" in data:
            results = RocketChatAPI.PlatformInterface.pi.rocketChatCreateChannel(data["platform_ID"],
                                                                                 data["subplatform_ID"],
                                                                                 data["channel_name"])
        elif "group_name" in data:
            results = RocketChatAPI.PlatformInterface.pi.rocketChatCreatePrivateGroup(data["platform_ID"],
                                                                                      data["subplatform_ID"],
                                                                                      data["group_name"])
        elif "user_ID" in data:
            results = RocketChatAPI.PlatformInterface.pi.rocketChatCreateUserToken(data["platform_ID"],
                                                                                   data["subplatform_ID"],
                                                                                   data["user_ID"], data["username"])
        else:
            results = RocketChatAPI.PlatformInterface.pi.rocketChatRegisterUser(data["platform_ID"],
                                                                                data["subplatform_ID"],
                                                                                data["user_email"], data["username"],
                                                                                data["user_pass"],
                                                                                data["user_nick"])
        if results is None:
            results = {"success": False}
        return results

    # rocketChatLoginUser(self, platform_ID, subPlatform_ID, username, user_pass)
    # rocketChatPostNewMessage(self, platform_ID, subPlatform_ID, room_ID, announcement)
    @staticmethod
    def put():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = rocketchat_user_login_request_schema.load(json_data)
        if errors:
            return errors, 422

        if "announcement" in data and "room_ID" in data:
            results = RocketChatAPI.PlatformInterface.pi.rocketChatPostNewMessage(data["platform_ID"],
                                                                                  data["subplatform_ID"],
                                                                                  data["room_ID"],
                                                                                  data["announcement"])
        else:
            results = RocketChatAPI.PlatformInterface.pi.rocketChatLoginUser(data["platform_ID"],
                                                                             data["subplatform_ID"],
                                                                             data["username"],
                                                                             data["user_pass"])
        if results is None:
            results = {"success": False}
        return results

    # rocketChatGetUserInfo(self, platform_ID, subPlatform_ID, user_ID, username)
    @staticmethod
    def get():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = rocketchat_user_get_request_schema.load(json_data)
        if errors:
            return errors, 422
        results = RocketChatAPI.PlatformInterface.pi.rocketChatGetUserInfo(data["platform_ID"], data["subplatform_ID"],
                                                                           data["user_ID"], data["username"])
        if results is None:
            results = {"success": False}
        return results

    # rocketChatDeleteUser(self, platform_ID, subPlatform_ID, user_ID)
    # rocketChatDeleteChannel(self, platform_ID, subPlatform_ID, channel_ID)
    # rocketChatDeletePrivateGroup(self, platform_ID, subPlatform_ID, room_ID)
    @staticmethod
    def delete():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = rocketchat_user_delete_request_schema.load(json_data)
        if errors:
            return errors, 422

        if "channel_ID" in data:
            results = RocketChatAPI.PlatformInterface.pi.rocketChatDeleteChannel(data["platform_ID"],
                                                                                 data["subplatform_ID"],
                                                                                 data["channel_ID"])
        elif "room_ID" in data:
            results = RocketChatAPI.PlatformInterface.pi.rocketChatDeletePrivateGroup(data["platform_ID"],
                                                                                      data["subplatform_ID"],
                                                                                      data["room_ID"])
        else:
            results = RocketChatAPI.PlatformInterface.pi.rocketChatGetUserInfo(data["platform_ID"],
                                                                               data["subplatform_ID"],
                                                                               data["user_ID"])
        if results is None:
            results = {"success": False}
        return results
