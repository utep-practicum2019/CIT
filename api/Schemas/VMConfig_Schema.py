from marshmallow import Schema, fields


class VMConfigSchema(Schema):
    vmName = fields.String()
    adpt_number = fields.String()
    src_ip = fields.String()
    dst_ip = fields.String()
    src_prt = fields.String()
    dst_prt = fields.String()
