from marshmallow import Schema, fields

# Used for Creating a Platform
class PlatformCreateRequestSchema(Schema):
    platform_name = fields.String(required=True)
    file_path = fields.String(required=True)
    ip_address = fields.String(required=True)
    port = fields.Int(required=True)

# Used for Modifying or Deleting a Platform
class PlatformRequestSchema(Schema):
    platform_name = fields.String()
    file_path = fields.String()
    ip_address = fields.String()
    port = fields.Int()
    command = fields.String()
    platform_id = fields.Int(required=True)

# Used for Responses
class PlatformResponseSchema(Schema):
    success = fields.Bool()

