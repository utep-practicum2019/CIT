from Schemas.Login_Schema import *

login_schema = LoginSchema()

from Schemas.VMConfig_Schema import *

vm_config_schema = VMConfigSchema()

from Schemas.VMStatus_Schema import *

vm_status_schema = VMStatusSchema()

from Schemas.VMStart_Schema import *

vm_start_schema = VMStartSchema()

from Schemas.VMSuspend_Schema import *

vm_suspend_schema = VMSuspendSchema()

from Schemas.User_Schema import *

user_schema = UserSchema()
user_request_schema = UserRequestSchema()
user_create_request_schema = UserCreateRequestSchema()
user_update_request_schema = UserUpdateRequestSchema()
user_response_schema = UserResponseSchema()

from Schemas.Group_Schema import *

group_request_schema = GroupRequestSchema()
group_update_request_schema = GroupUpdateRequestSchema()
group_response_schema = GroupResponseSchema()

from Schemas.Platform_Schema import *

platform_request_schema = PlatformRequestSchema()
platform_response_schema = PlatformResponseSchema()
platform_create_request_schema = PlatformCreateRequestSchema()

from Schemas.Connection_Schema import *

connection_request_schema = ConnectionRequestSchema()
connection_response_schema = ConnectionResponseSchema()

from Schemas.DatabaseSchema import *

database_document_schema = DatabaseDocumentSchema()
database_request_schema = DatabaseRequestSchema()
database_response_schema = DatabaseResponseSchema()
database_modify_schema = DatabaseModifySchema()

# class PlatformSchema(Schema):
#     platform_name = fields.String(required=True)
#     username = fields.String(required=True)
#     group_identifier = fields.Int(required=True)
#     task_type = fields.String(required=True)
#
#
# platform_schema = PlatformSchema()
