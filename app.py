from flask import Flask
from flask import render_template

app = Flask(__name__)





@app.route('/indexAdmin')
def indexAdminPage():
	return render_template('adminMenu/indexAdmin.html')

@app.route('/plat')
def platPage():
    return render_template('adminMenu/platMan.html')


@app.route('/acct')
def acctPage():
    return render_template('adminMenu/accountsMan.html')


@app.route('/connect')
def connectPage():
    return render_template('adminMenu/connectionMan.html')








    


if __name__ == '__main__':
    app.run()
