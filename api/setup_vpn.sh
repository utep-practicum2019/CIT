#!/bin/sh
#sudo pico -w /etc/pptpd.conf
sudo cat >> /etc/pptpd.conf<< END
localip 10.10.0.1
remoteip 10.10.0.2-100
END
#sudo pico -w /etc/ppp/pptpd-options
sudo cat >> /etc/ppp/pptpd-options<< END
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
END
#sudo pico -w /etc/ppp/chap-secrets
sudo cat >> /etc/ppp/chap-secrets << END
tempusr pptpd temppass *
END
#*allows for all IP
#sudo pico -w /etc/sysctl.conf
sudo cat >> /etc/sysctl.conf << END
net.ipv4.ip_forward=1
END
sudo sysctl -p
#sudo sysctl -psudo pico -w /etc/sysctl.conf
sudo iptables -t nat -A POSTROUTING -o etho0 -j MASQUERADE
sudo iptables -A FORWARD -i eth0 -o ppp0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i ppp0 -o eth0 -j ACCEPT
service pptpd restart
