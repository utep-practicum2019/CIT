#!/usr/bin/env bash
sudo apt-get install -f #for those vanilla versions without apt-get.  If installed it should simply move forward
sudo apt-get update -y
sudo apt-get install python3 -y
sudo apt-get install apache2 -y
sudo apt-get install libapache2-mod-wsgi-py3 -y
sudo apt-get install pptpd -y
sudo apt-get install curl -y 


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
cd wiki
sudo git clone https://github.com/Jermolene/TiddlyWiki5
sudo curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash - 
sudo apt-get install -y nodejs
sudo npm install http-server
cd ..



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
sudo apt-get update -y

sudo apt-get install -y mongodb-org
#sudo apt-get install -y mongodb-org --allow-unauthenticated
sudo service mongod start


#configuring the VPN
sudo su -c" cat >> /etc/pptpd.conf<< END
localip 10.10.0.1
remoteip 10.10.0.2-100
END"

sudo su -c " cat >> /etc/ppp/pptpd-options<< END
name pptpd
 refuse-pap
 refuse-chap
 refuse-mschap
 require-mschap-v2
 require-mppe-128
 ms-dns 8.8.8.8
 #ms-dns 8.8.4.4
 proxyarp
 nodefaultroute
 lock
 nobsdcomp
 mu 1490
 mru 1490
END"

sudo -c " cat >> /etc/ppp/chap-secrets << END
tempusr pptpd temppass *
END"
#*allows for all IP
sudo -c " cat >> /etc/sysctl.conf << END
net.ipv4.ip_forward=1
END"
sudo sysctl -p

sudo iptables -t nat -A POSTROUTING -o etho0 -j MASQUERADE
sudo iptables -A FORWARD -i eth0 -o ppp0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i ppp0 -o eth0 -j ACCEPT
sudo service pptpd restart

sudo su -c "echo 127.0.0.1 citsystem.com >> /etc/hosts"
sudo mv citsystem.com.conf /etc/apache2/sites-available
sudo a2ensite citsystem.com.conf
sudo /etc/init.d/apache2 restart

#rocketChat portion
sudo a2enmod proxy proxy_http rewrite
sudo snap install rocketchat-server
sudo mv Rocket.Chat.conf /etc/apache2/sites-available
sudo chmod 644 /etc/apache2/sites-available/Rocket.Chat.conf
sudo a2ensite Rocket.Chat
sudo service apache2 relaod

echo "CIT_server setup complete."
echo "Please type citsystem.com in your URL."
