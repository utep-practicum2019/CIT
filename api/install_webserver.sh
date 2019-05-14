#!/usr/bin/env bash

if [ "$(id -u)" == "0" ]; then 
    echo "install_webserver.sh should be ran as regular user, not sudo." 1>&2
    exit 1
fi

export CIT_IP=$(ip route get 8.8.8.8 | awk -F"src " 'NR==1{split($2,a," ");print a[1]}')
#export CIT_IP=$(ifconfig enp0s3 | grep 'inet addr:' | cut -d: -f2 | awk '{print $1}')
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

sudo snap install rocketchat-server

#virtual box
sudo apt-get install virtualbox -y
sudo apt-get install virtualbox-ext-pack -y

sudo mkdir ~/Desktop/hackathon_results

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

#L2TP
sudo add-apt repository ppa:nm-12tp/network-manager-l2tp
sudo apt-get update
sudo apt -y install network-manager-l2tp
sudo apt-get install network-manager-l2tp-gnome
sudo apt-get update

# Sudo gui prompt setup
sudo su -c 'echo "#!/usr/bin/env bash" >> /usr/local/bin/zenity_passphrase'
sudo su -c 'echo zenity --password --title="CIT sudo request" --timeout=10 >> /usr/local/bin/zenity_passphrase'
sudo chmod 777 /usr/local/bin/zenity_passphrase
sudo su -c 'echo Path askpass /usr/local/bin/zenity_passphrase >> /etc/sudo.conf'

# Apache configuration
sudo su -c "echo export CITPATH=/var/www/cit >> /etc/apache2/envvars"
sudo su -c "echo export CITPATH=/var/www/cit >> /etc/environment"
sudo su -c "echo export HOST=$CIT_IP >> /etc/apache2/envvars"
sudo su -c "echo export HOST=$CIT_IP >> /etc/environment"
sudo su -c "echo export DISPLAY=$DISPLAY>> /etc/apache2/envvars"


sudo su -c "echo '$CIT_IP citsystem.com' >> /etc/hosts"
sudo sed -i -e 's/INSERT_IP_HERE/'"$CIT_IP"':80/' citsystem.com.conf
#sudo sed -i -e 's/INSERT_USER_HERE/'"$SUDO_USER"'/' citsystem.com.conf
#sudo sed -i -e 's/INSERT_USER_HERE/'"$USER"'/' citsystem.com.conf
sudo sed -i -e 's/INSERT_USER_HERE/'"$USER"'/g' citsystem.com.conf
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

echo "install_webserver.sh setup complete."
echo "Please type citsystem.com in your URL."

