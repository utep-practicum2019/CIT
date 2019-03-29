from marshmallow import Schema, fields


# rocketChatRegisterUser(self, platform_ID, subplatforms_IDS, user_email, username, user_pass, user_nick)
# rocketChatCreateChannel(self, platform_ID, subplatforms_IDS, channel_name)
# rocketChatCreatePrivateGroup(self, platform_ID, subplatforms_IDS, group_name)
class RocketPOSTRequestSchema(Schema):
    platform_ID = fields.Integer()
    subplatforms_IDS = fields.List(fields.Integer())
    user_email = fields.String()
    username = fields.String()
    user_pass = fields.String()
    user_nick = fields.String()
    channel_name = fields.String()
    group_name = fields.String()
    user_ID = fields.String()


# rocketChatLoginUser(self, platform_ID, subplatforms_IDS, username, user_pass)
# rocketChatPostNewMessage(self, platform_ID, subplatforms_IDS, room_ID, announcement)
class RocketLOGINRequestSchema(Schema):
    platform_ID = fields.Integer()
    subplatforms_IDS = fields.List(fields.Integer())
    username = fields.String()
    user_pass = fields.String()
    announcement = fields.String()
    room_ID = fields.String()


# rocketChatGetUserInfo(self, platform_ID, subplatforms_IDS, user_ID, username)
class RocketGETRequestSchema(Schema):
    platform_ID = fields.Integer()
    subplatforms_IDS = fields.List(fields.Integer())
    user_ID = fields.String()
    username = fields.String()


# rocketChatDeleteUser(self, platform_ID, subplatforms_IDS, user_ID)
# rocketChatDeleteChannel(self, platform_ID, subplatforms_IDS, channel_ID)
# rocketChatDeletePrivateGroup(self, platform_ID, subplatforms_IDS, room_ID)
class RocketDELETERequestSchema(Schema):
    platform_ID = fields.Integer()
    subplatforms_IDS = fields.List(fields.Integer())
    user_ID = fields.String()
    channel_ID = fields.String()
    room_ID = fields.String()


rocketchat_user_post_request_schema = RocketPOSTRequestSchema()
rocketchat_user_login_request_schema = RocketLOGINRequestSchema()
rocketchat_user_get_request_schema = RocketGETRequestSchema()
rocketchat_user_delete_request_schema = RocketDELETERequestSchema()
