from flask import Flask, render_template, redirect, url_for, request, session, flash, send_from_directory
from werkzeug.utils import secure_filename
from Database.database_handler import DatabaseHandler
# from Platforms.Results import Results
import glob, os
import time


UPLOAD_FOLDER = '/home/practicum/Desktop/file_testing/to'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'pcap'])

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/home', methods=['GET', 'POST'])
def home():
    if session.get('logged_in') is None:
        return redirect(url_for('login'))

    username = session['username']
    group_id = session['group_id']
    remote_ip = session['remote_ip']

    group_info = DatabaseHandler.find('groups', group_id)
    #print ('Group Info -> {}'.format(group_info))

    try:
        platforms = group_info['platforms']
    except KeyError as e:
        print("No platform for user: ", username)
        return "You currently don't have access to any platforms bruh. Please contact us at support@cit.com >.<"
    #print('Group platforms available -> {}'.format(platforms))

    #platform_data = DatabaseHandler.find('platforms', platforms[0])
    #print('Subplatforms from database -> {}'.format(platform_data))

    ogList = []

    for p in platforms:
        platform_data = DatabaseHandler.find('platforms', p)
        subplats = platform_data['subplatforms']
        p = platform_data['main']['name']
        result = {p: []}
        for plat in subplats:
            result[p].append([plat['name'], plat['ip_port']])
        # print(result)

        ogList.append(result)

    from pprint import pprint
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
        file = request.files['file']
        print(file)
        print(file.filename)
        UserFile = file.filename
        file.filename = str(session['group_id']) + UserFile
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            send_from_directory(app.config['UPLOAD_FOLDER'], filename)
            return redirect(url_for('home'))

    # print(os.getcwd())
    read_directory = 'Download_Files'
    downloadable_files = get_downloadable_files(read_directory)
    os.chdir('../../')

    platform_names = []
    for plat in platforms:
            platform_names.append(DatabaseHandler.find('platforms', plat)['main']['name'])

    return render_template('index.html', username=username, platforms=platform_names, read_directory=read_directory,
                           downloadable_files=downloadable_files, ogList=ogList, remote_ip=remote_ip, team=team,
                           time=time)
    # return render_template('index.html', username=username, platforms=platforms, read_directory=read_directory,
    #                            downloadable_files=downloadable_files, ogList=ogList, remote_ip=remote_ip, team=team,
    #                             call=check_file_status(), time=time)


@app.route('/results/<filename>')
def results(filename):
    return render_template('results.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = DatabaseHandler.find('users', request.form['username'])
        if user is None or user['password'] != request.form['password']:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['username'] = request.form['username']
            session['group_id'] = user['group_id']
            session['remote_ip'] = user['remote_ip']
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    # session.pop('username', None)
    # session.pop('group_id', None)
    # session.pop('remote_ip', None)
    # session.pop('logged_in', None)
    session.clear()
    return redirect(url_for('index'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_downloadable_files(read_directory):
    os.chdir('static/{}'.format(read_directory))
    downloadable_files = []
    for file in glob.glob("*.*"):
        downloadable_files.append(file)

    #print('Inside the get_downloadable_files method -> {}'.format(os.getcwd()))

    return downloadable_files


def check_file_status():
    repeat = True

    while repeat:
        from PlatformManager.Platforms.SubPlatforms.Results import Results
        status = Results.getStatus(session['group_id'])
        time.sleep(60)
        if status:
            results = Results.getResults(session['group_id'])
            repeat = False
            return results



if __name__ == '__main__':
    app.run()


# Not in use anymore
# def get_platform(platform_id):
#     if platform_id == 'Hackathon':
#         return [
#                 {
#                     'name': 'chat',
#                     'ip': '129.108.7.17',
#                     'port': 3000
#
#                 },
#                 {
#                     'name': 'wiki',
#                     'ip':'129.108.7.17',
#                     'port': 8085
#
#                 },
#                 {
#                     'name': 'File Upload',
#
#                 },
#                 {
#                     'name': 'Download Files',
#                     'folderDirectory': 'Download_Files/' # Directory of where the files to download are going to be read from
#                 }
#             ]
#
#     if platform_id == 'Rapid Cyber Challenge':
#         return [
#             {
#                 'name': 'wiki',
#                 'ip': '129.108.7.17',
#                 'port': 8085
#
#             },
#             {
#                 'name': 'File Upload'
#             }
#         ]


# @app.route('/Upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         print(file)
#         print(file.filename)
#         UserFile = file.filename
#         file.filename = session['username'] + UserFile
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# @app.route('/api/v1.0/platforms/<string:username>', methods=['GET', 'PUT'])
# def get_user_platforms(username):
#     print('In the get_user_platforms route')
#     if username == 'JaneD':
#         return jsonify({"Hackathon": "This is the hackathon page", "Rapid Cyber": "This is the rapid cyber page"})
#     else:
#         return jsonify({"Hackathon": "This is the hackathon page"})