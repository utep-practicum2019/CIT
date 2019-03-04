from marshmallow import Schema, fields


class GroupSchema(Schema):
    group_id = fields.Int()
    min = fields.Int()
    max = fields.Int()
    platforms = fields.List(fields.String())
    members = fields.List(fields.String())
    chat_id = fields.Int()


class GroupRequestSchema(GroupSchema):
    group_id = fields.Int(required=True)


class GroupUpdateRequestSchema(Schema):
    group_id = fields.Int(required=True)
    updated_group = fields.Nested(GroupSchema, required=True)


class GroupResponseSchema(Schema):
    group_id = fields.Int()
    min = fields.Int()
    max = fields.Int()
    platforms = fields.List(fields.String())
    members = fields.List(fields.String())
    chat_id = fields.Int()
    success = fields.Bool(required=True)
