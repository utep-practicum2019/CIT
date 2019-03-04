from marshmallow import Schema, fields


class ConnectionRequestSchema(Schema):
    num_users = fields.Int()
    list_of_users = fields.List(fields.String())
    username = fields.String()
    password = fields.String()


# Used for Responses
class ConnectionResponseSchema(Schema):
    success = fields.Bool()
