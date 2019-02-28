from marshmallow import Schema, fields

class UserRequestSchema(Schema):
    username = fields.String(required=True)
    password = fields.String()
    newName = fields.String()
    group_id = fields.Int()
    connectionType = fields.String()


class UserCreateRequestSchema(UserRequestSchema):
    password = fields.String(required=True)
    internalIP = fields.String()


class UserResponseSchema(Schema):
    username = fields.String()
    password = fields.String()
    group_id = fields.Int()
    internalIP = fields.String()
    connectionType = fields.String()
    success = fields.Bool(required=True)

