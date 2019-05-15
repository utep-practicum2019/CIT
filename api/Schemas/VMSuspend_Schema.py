from marshmallow import Schema, fields


class VMSuspendSchema(Schema):
    vmName = fields.String(required=True)
