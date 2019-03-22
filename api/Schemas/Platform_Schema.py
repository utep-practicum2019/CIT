from marshmallow import Schema, fields


# Used for Creating a Platform
class PlatformCreateRequestSchema(Schema):
    platform_name = fields.String(required=True)
    file_path = fields.String(required=True)
    ip_address = fields.String(required=True)
    port = fields.Int(required=True)


# Used for POST requests
class PlatformPostRequestSchema(Schema):
    request = fields.String(required=True)
    name = fields.String(required=True)
    platform = fields.String()
    username = fields.String()
    email = fields.String()
    password = fields.String()


# Used for POST responses
class PlatformPostResponseSchema(Schema):
    destination = fields.String(required=True)
    response = fields.String(required=True)


# Used for GET requests
class PlatformGetRequestSchema(Schema):
    request = fields.String(required=True)
    platform = fields.String()
    requester = fields.String()


# Used for GET responses
class PlatformGetResponseSchema(Schema):
    destination = fields.String(required=True)
    response = fields.String(required=True)


# Used for Responses
class PlatformResponseSchema(Schema):
    success = fields.Bool()
