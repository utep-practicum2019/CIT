#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install python3
sudo apt-get install apache2 -y
sudo apt-get install libapache2-mod-wsgi-py3 -y

sudo mkdir /var/www/cit
sudo mv * /var/www/cit
cd /var/www/cit

sudo apt install python3-venv -y
sudo pyvenv test_bed_environment
source test_bed_environment/bin/activate
sudo apt-get install python3-pip -y
sudo chown -R $USER test_bed_environment


#install dependencies for request handler


pip install flask


pip install wheel

pip install flask-restful
pip install flask-marshmallow
pip install flask-httpauth
pip install flask-api
pip install pymongo
pip install pyinotify
pip install apispec
pip install apispec-webframeworks
pip install sockets
pip install requests
pip install jsonify
pip install resource
pip install schemas
#flask run

sudo su -c "echo 127.0.0.1 citsystem.com > /etc/hosts"
sudo mv citsystem.com.conf /etc/apache2/sites-available
sudo a2ensite citsystem.com.conf
sudo /etc/init.d/apache2 restart

echo "CIT_API setup complete."
echo "Please type citsystem.com in your URL."
