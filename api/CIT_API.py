from flask import Flask, send_file
# client gui
from flask import render_template, request, redirect
# User GUI
from flask import session, url_for, flash, send_from_directory
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_restful import Api
from werkzeug.utils import secure_filename
import glob
import os
import time
import datetime
from pprint import pprint

from Database.database_handler import DatabaseHandler
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
    # print('Group Info -> {}'.format(group_info))

    try:
        platforms = group_info['platforms']
    except KeyError as e:
        print("No platform for user: ", username)
        return 'You currently do not have access to any platforms bruh. Please contact us via the link provided ' \
               '<a href="https://bongo.cat/">support@cit.com</a> >.<'
    # print('Group platforms available -> {}'.format(platforms))

    ogList = create_ogList(platforms)
    # pprint(ogList)
    # print("^^^ogList")

    team = group_info['members']

    # Gets the downloadable files from the Downloads Directory
    main_directory = 'Downloads'
    downloadable_files = get_downloadables(main_directory)

    platform_names = []
    for plat in platforms:
        platform_names.append(DatabaseHandler.find('platforms', plat)['main']['name'])

    try:
        tmp = session['filename']
    except KeyError:
        session['filename'] = 'thatonefile.txt'

    return render_template('index.html', username=username, platforms=platform_names, main_directory=main_directory,
                           downloadable_files=downloadable_files, ogList=ogList, remote_ip=remote_ip, team=team,
                           time=time, platforms_id=platforms, group_id=group_id, filename=session['filename'])


@app.route('/fileUpload', methods=['GET', 'POST'])
def fileUpload():
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
        file.filename = str(session['group_id']) + currentDT.strftime("_%Y-%m-%d_%H-%M-%S") + "." + temp[len(temp) - 1]

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
            return session['filename']


@app.route('/<path>/<file_name>')
def download_file(path, file_name):
    path = path.replace('-', '/')
    return send_file(path + '/' + file_name, as_attachment=True)


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
    session.clear()
    session.pop('authToken', None)
    return redirect(url_for('index'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Currently not used. Old version of downloads platform.
def get_downloadable_files(read_directory):
    os.chdir('static/{}'.format(read_directory))
    downloadable_files = []
    for file in glob.glob("*"):
        downloadable_files.append(file)

    return downloadable_files


"""
    Method to create a dictionary to be used to dynamically create the 
    downloadable files that the user can download for the "Materials" 
    platform
    @var: main_directory - The directory that holds the subdirectories 
                           that have the files the user can download
    @return: Returns a dictionary that contains all the subdirectories 
             and their corresponding files 
"""
def get_downloadables(main_directory):
    cpy_root = ""
    downloadable_files = {}
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk(main_directory):
        cpy_root = root
        path = root.split(os.sep)
        # print(os.path.basename(root), "Level = " + str(len(path) - 1))
        f = []
        for file in files:
            f.append(file)
            cpy_root = cpy_root.replace('/', '-')
            downloadable_files.update( { cpy_root : f} )

    # pprint(downloadable_files)

    return downloadable_files

def create_ogList(platforms):
    ogList = []
    username = session['username']

    """
     The structure for the ogList the contains the main platform as the key and the subplatforms as lists and the lists
     for the subplatforms contains the subplatform name, ip and port, and the id that is associated with the 
     subplatform upon creation of the subplatform
        [
            {
              'Hackathon':
                    [
                        ['chat', '129.108.7.17:3000, '15321'],
                        ['wiki', '129.108.7.17:8085, '62147'],
                        ['File Upload']
                    ]    
            },
            {
              'Rapid Cyber Challenge':
                    [
                        [],
                        [],
                        []
                    ]
            }
        ]
    """

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
                token = platform_interface.rocketChatLoginUser(platform_data['main']['id'], plat['id'], username,
                                                               session['password'])
                session['authToken'] = token['Auth_Token']
                authTokens[plat['id']] = token
                session['authToken'] = token['Auth_Token']
        # print(result)

        ogList.append(result)

    return ogList


"""
    =========================================================================================
                                            ADMIN GUI    
    =========================================================================================
"""
allowed_ips = ["127.0.0.1"]

@app.route('/admin')
def main():
    print(request.environ['REMOTE_ADDR'])
    if request.environ['REMOTE_ADDR'] not in allowed_ips:
        return render_template('thouShallNotPass.html')
    return render_template('platMan.html')


@app.route('/accountsMan.html', methods=['GET', 'POST'])
def accountsMan():
    if request.environ['REMOTE_ADDR'] not in allowed_ips:
        return render_template('thouShallNotPass.html')

    if request.method == 'POST':
        return redirect("api/v2/resources/group", code=307)
    users = DatabaseHandler.find('users', None)
    groups = DatabaseHandler.find('groups', None)
    return render_template('accountsMan.html', username='Sara', group_num='2', users_group='4', group_id='1',
                           users=users, groups=groups)


@app.route('/connectionMan.html')
def addUsers():
    if request.environ['REMOTE_ADDR'] not in allowed_ips:
        return render_template('thouShallNotPass.html')
    return render_template('connectionMan.html')


@app.route('/platMan.html')
def platMan():
    if request.environ['REMOTE_ADDR'] not in allowed_ips:
        return render_template('thouShallNotPass.html')
    return render_template('platMan.html')


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
    # app.debug = True
    app.run(host="0.0.0.0", port=5001)
