from Login_Schema import *

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


from Platform_Schema import *

platform_request_schema = PlatformRequestSchema()
platform_response_schema = PlatformResponseSchema()
platform_create_request_schema = PlatformCreateRequestSchema()

from Connection_Schema import *

connection_request_schema = ConnectionRequestSchema()
connection_response_schema = ConnectionResponseSchema()

# class PlatformSchema(Schema):
#     platform_name = fields.String(required=True)
#     username = fields.String(required=True)
#     group_identifier = fields.Int(required=True)
#     task_type = fields.String(required=True)
#
#
# platform_schema = PlatformSchema()
