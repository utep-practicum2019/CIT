from marshmallow import Schema, fields, post_load

from AccountManager.user import User


class UserSchema(Schema):
    username = fields.String(required=True)
    password = fields.String()
    group_id = fields.Int()
    internal_ip = fields.String()
    remote_ip = fields.String()
    connectionType = fields.String()

    @post_load
    def make_user(self, data):
        return User(**data)


class UserRequestSchema(Schema):
    username = fields.String(required=True)


class UserUpdateRequestSchema(UserRequestSchema):
    updated_user = fields.Nested(UserSchema, required=True)


class UserCreateRequestSchema(Schema):
    group_count = fields.Integer(required=True)
    users_per_group = fields.Integer(required=True)
    filepath = fields.String()


class UserResponseSchema(UserSchema):
    success = fields.Boolean(required=True)


class UserDELETERequestSchema(Schema):
    list_of_users = fields.List(fields.String())


class UserGETRequestSchema(Schema):
    username = fields.String()


user_schema = UserSchema()
user_get_request_schema = UserGETRequestSchema()
user_request_schema = UserRequestSchema()
user_create_request_schema = UserCreateRequestSchema()
user_update_request_schema = UserUpdateRequestSchema()
user_response_schema = UserResponseSchema()
user_delete_request_schema = UserDELETERequestSchema()
