#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install python3
sudo apt-get install apache2 -y
sudo apt-get install libapache2-mod-wsgi-py3 -y
sudo apt-get install pptpd -y
sudo apt-get install curl -y #curl is needed


sudo mkdir /var/www/cit
sudo mv * /var/www/cit
cd /var/www/cit

mkdir /var/www/cit/wiki
cd wiki
git clone https://github.com/Jermolene/TiddlyWiki5

curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash - 


sudo apt-get install -y nodejs

npm install http-server
cd ..


sudo apt install python3-venv -y
sudo pyvenv test_bed_environment
source test_bed_environment/bin/activate
sudo apt-get install python3-pip -y
sudo chown -R $USER test_bed_environment



pip install flask

#export FLASK_APP=CIT_API

pip install flask-restful
pip install flask-marshmallow
pip install flask-httpauth
pip install flask-api

pip install pyinotify
pip install apispec
pip install apispec-webframeworks
pip install sockets
pip install requests
pip install jsonify
pip install resource
pip install schemas
#flask run


pip install pymongo
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
sudo apt-get update

sudo apt-get install -y mongodb-org
#sudo apt-get install -y mongodb-org --allow-unauthenticated
sudo service mongod start
sudo su -c "echo 127.0.0.1 citsystem.com >> /etc/hosts"
sudo mv citsystem.com.conf /etc/apache2/sites-available
sudo a2ensite citsystem.com.conf
sudo /etc/init.d/apache2 restart

echo "CIT_API setup complete."
echo "Please type citsystem.com in your URL."
