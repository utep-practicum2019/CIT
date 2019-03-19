from marshmallow import Schema, fields


class ConnectionRequestSchema(Schema):
    num_users = fields.Int()
    list_of_users = fields.List(fields.String())
    username = fields.String()
    password = fields.String()


# Used for Responses
class ConnectionResponseSchema(Schema):
    success = fields.Bool()


class ConnectionUserSchema(Schema):
    username = fields.String()
    password = fields.String()
    pptpIP = fields.String()


class ConnectionGetRequestSchema(Schema):
    session_list = fields.Boolean()


class ConnectionPostRequestSchema(Schema):
    usernames = fields.List(fields.String())
    num_users = fields.Integer()


class ConnectionPostResponseSchema(Schema):
    usersDictionary = fields.Nested(ConnectionUserSchema, many=True)


class ConnectionDeleteRequestSchema(Schema):
    list_of_users = fields.List(fields.String())


class ConnectionPutRequestSchema(Schema):
    currUsername = fields.String()
    newUsername = fields.String()
    newPassword = fields.String()
    newIP = fields.String()


connection_get_request_schema = ConnectionGetRequestSchema()
connection_post_request_schema = ConnectionPostRequestSchema()
connection_post_response_schema = ConnectionPostResponseSchema()
connection_delete_request_schema = ConnectionDeleteRequestSchema()
connection_put_request_schema = ConnectionPutRequestSchema()
connection_response_schema = ConnectionResponseSchema()
