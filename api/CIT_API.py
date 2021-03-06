from flask import Flask, send_file
# client gui
from flask import render_template, request, redirect
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_restful import Api

# User GUI
from flask import session, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import glob
import os, sys
import time
import datetime
from pprint import pprint


from Database.database_handler import DatabaseHandler
from PlatformManager.PlatformInterface import  PlatformInterface
from Resources.ConnectionResource import ConnectionAPI
from Resources.DatabaseResource import DatabaseAPI
from Resources.GroupResource import GroupAPI
from Resources.LoginResource import LoginAPI
from Resources.PlatformResource import PlatformAPI
from Resources.RocketChatResource import RocketChatAPI
from Resources.UserResource import UserAPI
from Resources.PlatformManagerInstance import PlatformManagerInstance

ma = Marshmallow()
app = Flask(__name__, static_folder='static',
            template_folder='templates')
app.secret_key = "turtles are the best!"
api = Api(app)
CORS(app)




api.add_resource(DatabaseAPI, '/api/v2/resources/database')
api.add_resource(ConnectionAPI, '/api/v2/resources/connection')
api.add_resource(UserAPI, '/api/v2/resources/user')
api.add_resource(GroupAPI, '/api/v2/resources/group')
api.add_resource(PlatformAPI, '/api/v2/resources/platform')
api.add_resource(RocketChatAPI, '/api/v2/resources/platform/rocketchat')

api.add_resource(LoginAPI, '/api/v2/resources/login')


"""
    =========================================================================================
                                            USER GUI    
    =========================================================================================
"""
UPLOAD_FOLDER = '/home/practicum/Desktop/hackathon_submissions'
ALLOWED_EXTENSIONS = set(['rules', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'pcap'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/rocketchat_api')
def rocketchat_api():
    str = "<script> " \
          "window.parent.postMessage({" \
          "event: 'login-with-token'," \
          "loginToken: '" + session['authToken'] + "'" \
          "}, 'http://0.0.0.0:3000');" \
          "</script>"
    return str

@app.route('/home', methods=['GET', 'POST'])
def home():
    if session.get('logged_in') is None:
        return redirect(url_for('login'))

    username = session['username']
    group_id = session['group_id']
    remote_ip = session['remote_ip']

    group_info = DatabaseHandler.find('groups', group_id)
    print ('Group Info -> {}'.format(group_info))

    try:
        platforms = group_info['platforms']
    except KeyError as e:
        print("No platform for user: ", username)
        return 'You currently do not have access to any platforms bruh. Please contact us via the link provided <a href="https://searchengineland.com/guide/how-to-use-google-to-search">support@cit.com</a> >.<'
    print('Group platforms available -> {}'.format(platforms))

    # platform_data = DatabaseHandler.find('platforms', platforms[0])
    # print('Subplatforms from database -> {}'.format(platform_data))

    ogList = []

    authTokens = {}
    for p in platforms:
        platform_data = DatabaseHandler.find('platforms', p)
        subplats = platform_data['subplatforms']
        p = platform_data['main']['name']
        result = {p: []}
        for plat in subplats:
            result[p].append([plat['name'], plat['ip_port'], plat['id']])
            if plat['name'] == "Rocketchat":
                platform_interface = PlatformManagerInstance.get_instance().platform_interface
                token = platform_interface.rocketChatLoginUser(platform_data['main']['id'], plat['id'], username, session['password'])
                session['authToken'] = token['Auth_Token']
                authTokens[plat['id']] = token
                session['authToken'] = token['Auth_Token']
        # print(result)

        ogList.append(result)


    pprint(ogList)
    print("^^^ogList")
    """
    [
        {
          'Hackathon':
                [
                    ['chat', '129.108.7.17:3000],
                    ['wiki', '129.108.7.17:8085],
                    ['File Upload']
                ]    
        },
        {
          'Rapid Cyber Challenge':

        }
    ]
    """
    team = group_info['members']
    # print(team)

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        # Gets the file and renames it to "Data_Time_GroupId.extensionType
        file = request.files['file']
        user_file = file.filename
        temp = user_file.split('.')
        currentDT = datetime.datetime.now()
        file.filename = str(session['group_id']) + currentDT.strftime("_%Y-%m-%d_%H-%M-%S") + "." + temp[len(temp)-1]

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            send_from_directory(app.config['UPLOAD_FOLDER'], filename)
            session['filename'] = file.filename[:-5] + "txt"
            return redirect(url_for('home'))


    #read_directory = 'Download_Files'
    #downloadable_files = get_downloadable_files(read_directory)
    #os.chdir('../../')

    # Test the test_get_downloadables method
    main_directory = 'Download_Files'
    downloadable_files = test_get_downloadables(main_directory)

    platform_names = []
    for plat in platforms:
        platform_names.append(DatabaseHandler.find('platforms', plat)['main']['name'])

    try:
        tmp = session['filename']
    except KeyError:
        session['filename'] = 'thatonefile.txt'
    return render_template('index.html', username=username, platforms=platform_names, main_directory=main_directory,
                           downloadable_files=downloadable_files, ogList=ogList, remote_ip=remote_ip, team=team,
                           time=time, platforms_id=platforms, filename=session['filename'])
    # return render_template('index.html', username=username, platforms=platforms, read_directory=read_directory,
    #                            downloadable_files=downloadable_files, ogList=ogList, remote_ip=remote_ip, team=team,
    #                             call=check_file_status(), time=time)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = DatabaseHandler.find('users', request.form['username'])
        if user is None or user['password'] != request.form['password']:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            session['group_id'] = user['group_id']
            session['remote_ip'] = user['remote_ip']
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    # remove the username, group_id, remote_ip, and logged_in from the session if it is there
    # session.pop('username', None)
    # session.pop('group_id', None)
    # session.pop('remote_ip', None)
    # session.pop('logged_in', None)

    #platform_interface = PlatformManagerInstance.get_instance().platform_interface
    # success, msg = platform_interface.logoutUser({'authToken': session['authToken']})

    # from rocketchat_API.rocketchat import RocketChat
    # rocket = RocketChat('Admin', 'chat.service', server_url='http://localhost:3000', proxies=None)
    # data = rocket.logout(authToken=session['authToken']).json()
    # status = data["status"]
    # msg = data['data']['message']
    # print(status, " ", msg)

    session.clear()
    session.pop('authToken', None)
    return redirect(url_for('index'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_downloadable_files(read_directory):
    os.chdir('static/{}'.format(read_directory))
    downloadable_files = []
    for file in glob.glob("*"):
        downloadable_files.append(file)

    # print('Inside the get_downloadable_files method -> {}'.format(os.getcwd()))

    return downloadable_files


"""
    Method to create a dictionary to be used to dynamically create the 
    downloadable files that the user can download for the "Materials" 
    platform
    @var: main_directory - The directory that holds the subdirectories 
                           that have the files the user can download
    @return: Returns a dictionary that contains all the subdirectories 
             their corresponding files 
"""
def test_get_downloadables(main_directory):
    root = "/home/practicum/Desktop/latest/integration/api/{}".format(main_directory)
    #path = os.path.join(root, "{}".format(main_directory))
    print("The following files are contained in the {}".format(main_directory))
    downloadable_files = {}
    for path, subdirs, files in os.walk(root):
        print(subdirs)
        for sd in subdirs:
            print(sd)
            if sd != 'css' or sd != 'js:':
                f = []
                os.chdir('{}/{}'.format(main_directory, sd))
                for file in glob.glob("*"):
                    print(sd+"/"+file)
                    f.append(file)
                downloadable_files.update( {sd : f} )
                os.chdir('../../')

    return downloadable_files


@app.route('/<main_dir>/<directory>/<file_name>')
def download_file(main_dir, directory, file_name):
    return send_file(main_dir+'/'+directory+'/'+file_name, as_attachment=True)





"""------- ADMIN WEB APP -------"""


@app.route('/admin')
def main():
    return render_template('platMan.html')


@app.route('/accountsMan.html', methods=['GET', 'POST'])
def accountsMan():
    if request.method == 'POST':
        return redirect("api/v2/resources/group", code=307)
    users = DatabaseHandler.find('users', None)
    groups = DatabaseHandler.find('groups', None)
    return render_template('accountsMan.html', username='Sara', group_num='2', users_group='4', group_id='1',
                           users=users, groups=groups)


@app.route('/connectionMan.html')
def addUsers():
    return render_template('connectionMan.html')


@app.route('/platMan.html')
def platMan():
    return render_template('platMan.html')


@app.route('/indexAdmin.html')
def index_admin():
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
    app.run(host="0.0.0.0", port=5001)
