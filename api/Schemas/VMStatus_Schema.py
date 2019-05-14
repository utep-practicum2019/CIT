from marshmallow import Schema, fields

class VMStatusSchema(Schema):
    vmName = fields.String(required=True)
    mgrStatus = fields.String()
