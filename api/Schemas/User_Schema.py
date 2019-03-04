from marshmallow import Schema, fields


class UserSchema(Schema):
    username = fields.String(required=True)
    password = fields.String()
    group_id = fields.Int()
    internal_ip = fields.String()
    remote_ip = fields.String()
    connectionType = fields.String()


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
