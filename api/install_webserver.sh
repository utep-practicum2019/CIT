#!/usr/bin/env bash
if [ -z "$CIT_IP" ]; then
    echo "CIT_IP must be set with the server ip address."
    echo "Use: export CIT_IP=<ip address>"
    exit 1
fi

sudo apt-get install -f #for those vanilla versions without apt-get.  If installed it should simply move forward
sudo add-apt-repository universe # enable community software
sudo apt-get update -y
sudo apt-get install python3 -y
sudo apt-get install apache2 -y
sudo apt-get install libapache2-mod-wsgi-py3 -y
sudo apt-get install pptpd -y
sudo apt-get install curl -y 
sudo apt install kdesudo -y
sudo snap install rocketchat-server

sudo mkdir /var/www/cit
sudo mv * /var/www/cit
cd /var/www/cit




sudo apt install python3-venv -y
sudo pyvenv test_bed_environment
source test_bed_environment/bin/activate
sudo apt-get install python3-pip -y
sudo chown -R $USER test_bed_environment

#wiki installer
sudo mkdir /var/www/cit/wiki
sudo mv /var/www/cit/genericWiki /var/www/cit/wiki
cd wiki
sudo git clone https://github.com/Jermolene/TiddlyWiki5
cd TiddlyWiki5

sudo curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash - 
sudo apt-get install -y nodejs
sudo npm install -g http-server
sudo npm i http-server
cd /var/www/cit

pip install --upgrade pip 
pip install flask

#export FLASK_APP=CIT_API

pip install flask-restful
pip install flask-marshmallow
pip install flask-httpauth
pip install flask-api
pip install flask-cors

pip install pyinotify
pip install apispec
pip install apispec-webframeworks
pip install sockets
pip install requests
pip install jsonify
pip install resource
pip install schemas
pip install mechanize
#flask run


pip install pymongo
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
sudo apt-get update -y

sudo apt-get install -y mongodb-org
sudo sed -i -e 's/port: 27017/port: 27018/g' /etc/mongod.conf
sudo sed -i -e 's/bindIp: 127.0.0.1/bindIp: '"$CIT_IP"'/g' /etc/mongod.conf
#sudo apt-get install -y mongodb-org --allow-unauthenticated
sudo service mongod start

sudo chmod 777 /etc/ppp/chap-secrets
sudo chmod 777 /etc
sudo chmod 777 /var/www/cit/next_group_id.txt
sudo chmod 777 /var/www/cit/configTempFile.txt

sudo chmod 777 /var/www/cit/PPTP_session_output.txt
sudo chmod 777 /var/www/cit/PPTP_session.txt


#configuring the VPN
sudo su -c "localip 192.168.0.1  >> /etc/pptpd.conf"
sudo su -c "remoteip 192.168.0.2-254 >> /etc/pptpd.conf"
sudo sed -i -e 's/#\?net.ipv4.ip_forward=[0,1]/net.ipv4.ip_forward=1/' /etc/sysctl.conf
sudo service pptpd restart


sudo su -c "echo export CITPATH=/var/www/cit >> /etc/apache2/envvars"
sudo su -c "echo export CITPATH=/var/www/cit >> /etc/environment"

sudo su -c "echo export HOST=$CIT_IP >> /etc/apache2/envvars"
sudo su -c "echo export HOST=$CIT_IP >> /etc/environment"

sudo su -c "echo '$CIT_IP citsystem.com' >> /etc/hosts"
sudo sed -i -e 's/INSERT_IP_HERE/'"$CIT_IP"':80/' citsystem.com.conf
sudo mv citsystem.com.conf /etc/apache2/sites-available
sudo a2ensite citsystem.com.conf
sudo /etc/init.d/apache2 restart

#rocketChat portion
sudo a2enmod proxy proxy_http rewrite

pip install rocketchat_API
sudo sed -i -e 's/INSERT_IP_HERE/'"$CIT_IP"'/' Rocket.Chat.conf
sudo mv Rocket.Chat.conf /etc/apache2/sites-available
sudo chmod 644 /etc/apache2/sites-available/Rocket.Chat.conf
sudo a2ensite Rocket.Chat
sudo service apache2 reload

sudo apt-get update -y

echo "CIT_server setup complete."
echo "Please type citsystem.com in your URL."

