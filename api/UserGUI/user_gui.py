# client gui
from flask import render_template, redirect, url_for, request, session, send_file
from Database.database_handler import DatabaseHandler


def index():
    return redirect(url_for('login'))


def home():
    if session.get('logged_in') is None:
        return redirect(url_for('login'))
    username = session['username']
    group_id = session['group_id']
    remote_ip = session['remote_ip']

    group_info = DatabaseHandler.find('groups', group_id)
    print (group_info)

    platforms = group_info['platforms']
    print(platforms)
    team = group_info['members']
    print(team)

    return render_template('index.html', username=username, platforms=platforms, remote_ip=remote_ip, team=team, re=re)


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


def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    session.pop('group_id', None)
    session.pop('logged_in', None)
    return redirect(url_for('index'))

