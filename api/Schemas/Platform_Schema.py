from marshmallow import Schema, fields


class PlatformPOSTRequestSchema(Schema):
    main_platform = fields.String()
    subplatforms = fields.List(fields.String())


class PlatformCOMMANDRequestSchema(Schema):
    command = fields.String()
    platform_ID = fields.Integer()
    subplatforms_IDS = fields.List(fields.Integer())
    configuration = fields.Dict()


class PlatformDELETERequestSchema(Schema):
    platform_ID = fields.Integer()
    subplatforms_IDS = fields.List(fields.Integer())


class PlatformGETRequestSchema(Schema):
    all = fields.Boolean()
    status = fields.Boolean()
    platform_ID = fields.Integer()


class PlatformPUTRequestSchema(Schema):
    platform_ID = fields.Integer(required=True)
    note = fields.String()
    alias = fields.String()
    subplatforms = fields.List(fields.String())


platform_put_request_schema = PlatformPUTRequestSchema()
platform_post_request_schema = PlatformPOSTRequestSchema()
platform_command_request_schema = PlatformCOMMANDRequestSchema()
platform_delete_request_schema = PlatformDELETERequestSchema()
platform_get_request_schema = PlatformGETRequestSchema()
