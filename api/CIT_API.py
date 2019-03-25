from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api

# client gui
from flask import render_template, redirect, url_for, request, session, send_file
from Database.database_handler import DatabaseHandler

from Resources.ConnectionResource import ConnectionAPI
from Resources.DatabaseResource import DatabaseAPI
from Resources.GroupResource import GroupAPI
from Resources.LoginResource import LoginAPI
from Resources.PlatformResource import PlatformAPI
from Resources.RocketChatResource import RocketChatAPI
from Resources.UserResource import UserAPI
from Resources.VMResource import VMConfigAPI, VMStartAPI, VMStatusAPI, VMSuspendAPI

ma = Marshmallow()
app = Flask(__name__)
app.secret_key = "turtles are the best!"
api = Api(app)

api.add_resource(DatabaseAPI, '/api/v2/resources/database')
api.add_resource(ConnectionAPI, '/api/v2/resources/connection')
api.add_resource(UserAPI, '/api/v2/resources/user')
api.add_resource(GroupAPI, '/api/v2/resources/group')
api.add_resource(PlatformAPI, '/api/v2/resources/platform')
api.add_resource(RocketChatAPI, '/api/v2/resources/platform/rocketchat')

api.add_resource(VMConfigAPI, '/api/v2/resources/vm/manage/config')
api.add_resource(VMStatusAPI, '/api/v2/resources/vm/manage/status')
api.add_resource(VMStartAPI, '/api/v2/resources/vm/manage/start')
api.add_resource(VMSuspendAPI, '/api/v2/resources/vm/manage/suspend')

api.add_resource(LoginAPI, '/api/v2/resources/login')


"""------- USER WEB APP -------"""
from UserGUI import user_gui


@app.route('/')
def index():
    return user_gui.index()


@app.route('/home')
def home():
    return user_gui.home()


@app.route('/login', methods=['GET', 'POST'])
def login():
    return user_gui.login()


@app.route('/logout')
def logout():
    return user_gui.logout()


"""------- ADMIN WEB APP -------"""
from AccountManager.account_manager import AccountManager


@app.route('/admin')
def main():
    return render_template('indexAdmin.html')


@app.route('/accountsMan.html', methods=['GET', 'POST'])
def accountsMan():
    users = DatabaseHandler.find('users', None)
    print(users)
    groups = DatabaseHandler.find('groups', None)
    print(groups)
    if request.method == 'POST':
        if request.form['group_num'] == '99' and request.form['users_group'] == '99' and request.form['username'] == '99':
            print("Delete is working")
        elif request.form['group_num'] is not None and request.form['users_group'] is not None:
            print("POST is working")
            print(int(request.form['group_num']))
            print(int(request.form['users_group']))
            x = AccountManager.create_groups(int(request.form['group_num']), int(request.form['users_group']))
            y = AccountManager.create_groups(int(request.form['group_num']), int(request.form['users_group']))
            print("hello "+str(y))
            # print("Username: " + request.form['username'])
    return render_template('accountsMan.html', username='Sara', group_num='2', users_group='4', users=users, groups=groups)


@app.route('/connectionMan.html')
def addUsers():
    return render_template('connectionMan.html')


@app.route('/platMan.html')
def platMan():
    return render_template('platMan.html')


@app.route('/indexAdmin.html')
def indexAdmin():
    return render_template('indexAdmin.html')


@app.route('/json-example')
def jsonexample():
    return 'Todo...'


@app.route('/query-example')
def queryexample():
    language = request.args.get('language')  # if key doesn't not exist, returns None
    framework = request.args.get('framework')
    website = request.args.get('website')
    return '''<h1>The language value is: {}</h1>
                <h1>The language value is: {}</h1>
                <h1>The language value is: {}</h1>'''.format(language, framework, website)


@app.route('/form-example', methods=['GET', 'POST'])  # allow both GET and POST requests
def formexample():
    if request.method == 'POST':
        # this block is only entered when the form is submitted
        language = request.form.get('Language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                Language: <input type="text" name"language"><br>
                Framework: <input type="text" name"framework"><br>
                <input type="submit" value="Submit"><br>
            </form>'''


if __name__ == '__main__':
    #app.run(host="citsystem.com", port=80)
    app.run(host="0.0.0.0", port=80)
