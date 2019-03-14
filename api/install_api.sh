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

pip install flask
pip install flask-restful

sudo su -c "echo 127.0.0.1 citsystem.com > /etc/hosts"
sudo mv citsystem.com.conf /etc/apache2/sites-available
sudo a2ensite citsystem.com.conf
sudo /etc/init.d/apache2 restart
