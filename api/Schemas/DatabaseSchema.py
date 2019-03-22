from marshmallow import (Schema, validates_schema, fields)

from Schemas.Group_Schema import GroupSchema
from Schemas.User_Schema import UserSchema


class DatabaseDocumentSchema(Schema):
    group = fields.Nested(GroupSchema)
    user = fields.Nested(UserSchema)

    @validates_schema
    def validate_at_least_one(self, data):
        if 'group' not in data and 'user' not in data:
            return 'Server could not complete your request'


class DatabaseRequestSchema(Schema):
    collection_name = fields.String(required=True)
    document_id = fields.String(required=True)


class DatabaseModifySchema(DatabaseRequestSchema):
    document = fields.Nested(DatabaseDocumentSchema, required=True)


class DatabaseResponseSchema(Schema):
    success = fields.Boolean()
