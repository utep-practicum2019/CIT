from Login_Schema import *
from marshmallow import Schema, fields

login_schema = LoginSchema()

from VMConfig_Schema import *

vm_config_schema = VMConfigSchema()

from VMStatus_Schema import *

vm_status_schema = VMStatusSchema()

from VMStart_Schema import *

vm_start_schema = VMStartSchema()

from VMSuspend_Schema import *

vm_suspend_schema = VMSuspendSchema()

from User_Schema import *

user_request_schema = UserRequestSchema()
user_create_request_schema = UserCreateRequestSchema()
user_response_schema = UserResponseSchema()

from Group_Schema import *

group_request_schema = GroupRequestSchema()
group_response_schema = GroupResponseSchema()


class PlatformSchema(Schema):
    platform_name = fields.String(required=True)
    username = fields.String(required=True)
    group_identifier = fields.Int(required=True)
    task_type = fields.String(required=True)


platform_schema = PlatformSchema()
