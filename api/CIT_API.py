from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api

from Resources.ConnectionResource import ConnectionAPI
from Resources.DatabaseResource import DatabaseAPI
from Resources.GroupResource import GroupAPI
from Resources.LoginResource import LoginAPI
# from Resources.PlatformResource import PlatformAPI
from Resources.UserResource import UserAPI
from Resources.VMResource import VMConfigAPI, VMStartAPI, VMStatusAPI, VMSuspendAPI

ma = Marshmallow()
app = Flask(__name__)
api = Api(app)

api.add_resource(DatabaseAPI, '/api/v2/resources/database')
api.add_resource(ConnectionAPI, '/api/v2/resources/connection')
api.add_resource(UserAPI, '/api/v2/resources/user')
api.add_resource(GroupAPI, '/api/v2/resources/group')
# api.add_resource(PlatformAPI, '/api/v2/resources/platform')

api.add_resource(VMConfigAPI, '/api/v2/resources/vm/manage/config')
api.add_resource(VMStatusAPI, '/api/v2/resources/vm/manage/status')
api.add_resource(VMStartAPI, '/api/v2/resources/vm/manage/start')
api.add_resource(VMSuspendAPI, '/api/v2/resources/vm/manage/suspend')

api.add_resource(LoginAPI, '/api/v2/resources/login')

if __name__ == '__main__':
    app.run()
