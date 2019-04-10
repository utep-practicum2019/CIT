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
    command = fields.String()
    group_id = fields.Int(required=True)
    platform_id = fields.Integer()
    platform_ids = fields.List(fields.Integer())
    updated_group = fields.Nested(GroupSchema)



class GroupResponseSchema(Schema):
    success = fields.Bool(required=True)


class GroupGetRequestSchema(Schema):
    group_id = fields.Int(required=True)


class GroupDELETERequestSchema(Schema):
    list_of_groups = fields.List(fields.Integer())


group_get_request_schema = GroupGetRequestSchema()
group_schema = GroupSchema()
group_request_schema = GroupRequestSchema()
group_update_request_schema = GroupUpdateRequestSchema()
group_response_schema = GroupResponseSchema()
group_delete_request_schema = GroupDELETERequestSchema()
