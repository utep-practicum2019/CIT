from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def main():
	return render_template('indexAdmin.html')

@app.route('/connectionMan.html')
def connectionMan():
	return render_template('connectionMan.html')
 
@app.route('/accountsMan.html')
def accountsMan():
	return render_template('accountsMan.html')

@app.route('/platMan.html')
def platMan():
	return render_template('platMan.html')

@app.route('/indexAdmin.html')
def indexAdmin():
	return render_template('indexAdmin.html')
	
if __name__ == "__main__":
	app.run()