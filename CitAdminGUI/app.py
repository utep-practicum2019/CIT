from flask import Flask, render_template, request, url_for, request, session, flash
import re
from API.AccountManager.account_manager import AccountManager
from Database.database_handler import DatabaseHandler

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def main():
    return render_template('indexAdmin.html')


@app.route('/connectionMan.html')
def connectionMan():
    return render_template('connectionMan.html')


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
            #print("Username: " + request.form['username'])
    return render_template('accountsMan.html', username = 'Sara', group_num = '2', users_group ='4', users = users, groups = groups )


@app.route('/addUsers.html')
def addUsers():
    return render_template('addUsers.html')


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
    if request.method == 'POST':  # this block is only entered when the form is submitted
        language = request.form.get('Language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
				  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
			  Language: <input type="text" name"language"><br>
			  Framework: <input type="text" name"framework"><br>
			  <input type="submit" value="Submit"><br>
			</form>'''


if __name__ == "__main__":
    app.run()