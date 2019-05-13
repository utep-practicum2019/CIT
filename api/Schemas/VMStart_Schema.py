from marshmallow import Schema, fields


class VMStartSchema(Schema):
    vmName = fields.String(required=True)
