from marshmallow import Schema, fields

class GroupRequestSchema(Schema):
    group_id = fields.String(required=True)
    min = fields.Int()
    max = fields.Int()
    platforms = fields.List(fields.String())
    members = fields.List(fields.String())
    chat_id = fields.Int()


class GroupResponseSchema(Schema):
    group_id = fields.String()
    min = fields.Int()
    max = fields.Int()
    platforms = fields.List(fields.String())
    members = fields.List(fields.String())
    chat_id = fields.Int()
    success = fields.Bool(required=True)
