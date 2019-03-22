# from CIT_API import *
# from apispec import APISpec
# from apispec.ext.marshmallow import MarshmallowPlugin
# from apispec_webframeworks.flask import FlaskPlugin
#
# spec = APISpec(
#     title="CITAPI",
#     version="2.0.0",
#     openapi_version="3.0.2",
#     info=dict(description="An early API for the CIT"),
#     plugins=[FlaskPlugin(), MarshmallowPlugin()],
# )
#
# # Reference your schemas definitions
# from CIT_API_Schema import *
#
# spec.components.schema('Login', schema=LoginSchema)
# spec.components.schema('Config', schema=VMConfigSchema)
# spec.components.schema('Status', schema=VMStatusSchema)
# spec.components.schema('Start', schema=VMStartSchema)
# spec.components.schema('Suspend', schema=VMSuspendSchema)
# spec.components.schema('Platform', schema=PlatformSchema)
#
# from pprint import pprint
#
# pprint(spec.to_dict())
#
# login_view = LoginAPI.as_view("login_view")
# app.add_url_rule("/api/v2/resources/login", view_func=login_view)
# with app.test_request_context():
#     spec.path(view=login_view, path='/api/v2/resources/login')
# # pprint(dict(spec.to_dict()["paths"]["/api/v2/resources/login"]))
