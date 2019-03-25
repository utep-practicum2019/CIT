from marshmallow import Schema, fields


class PlatformPOSTRequestSchema(Schema):
    main_platform = fields.String()
    subplatforms = fields.List(fields.String())


class PlatformADDRequestSchema(Schema):
    platform_ID = fields.Integer()
    subplatforms = fields.List(fields.String())


class PlatformCOMMANDRequestSchema(Schema):
    command = fields.String()
    platform_ID = fields.Integer()
    subplatforms_IDS = fields.List(fields.Integer())


class PlatformDELETERequestSchema(Schema):
    platform_ID = fields.Integer()
    subplatforms_IDS = fields.List(fields.Integer())


platform_post_request_schema = PlatformPOSTRequestSchema()
platform_add_request_schema = PlatformADDRequestSchema()
platform_command_request_schema = PlatformCOMMANDRequestSchema()
platform_delete_request_schema = PlatformDELETERequestSchema()
