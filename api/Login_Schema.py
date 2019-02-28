from marshmallow import Schema, fields

class LoginSchema(Schema):
    ip = fields.String(required=True)