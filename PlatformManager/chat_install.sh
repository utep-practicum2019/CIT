# Ensure all packages are up to date:
 apt-get update

# Install snapd apache2 and Rocket Chat:
apt-get install snapd apache2 -y ; snap install rocketchat-server

# Start and enable Apache2:
systemctl start apache2 ; systemctl enable apache2

# Ensure Apache2 modules are enabled :
a2enmod proxy proxy_http rewrite

# Configure Rocket.Chat:
cd Desktop/RC
mv Rocket.Chat.conf /etc/apache2/sites-available
cd
chmod 644 /etc/apache2/sites-available/Rocket.Chat.conf
apache2ctl comfigtest
a2dissite 000-default.conf
a2ensite Rocket.Chat
netstat -tlpn | grep 3000
hostname -I

# Restart
systemctl reload apache2
