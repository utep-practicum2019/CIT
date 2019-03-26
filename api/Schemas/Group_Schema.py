from marshmallow import Schema, fields, post_load

from AccountManager.group import Group


class GroupSchema(Schema):
    group_id = fields.Int()
    min = fields.Int()
    max = fields.Int()
    platforms = fields.List(fields.String())
    members = fields.List(fields.String())
    chat_id = fields.Int()

    @post_load
    def make_group(self, data):
        return Group(**data)


class GroupRequestSchema(GroupSchema):
    group_id = fields.Int(required=True)


class GroupUpdateRequestSchema(Schema):
    group_id = fields.Int(required=True)
    platform_name = fields.String()
    updated_group = fields.Nested(GroupSchema)


class GroupResponseSchema(Schema):
    success = fields.Bool(required=True)


class GroupGetRequestSchema(Schema):
    group_id = fields.Int(required=True)


group_get_request_schema = GroupGetRequestSchema()
group_schema = GroupSchema()
