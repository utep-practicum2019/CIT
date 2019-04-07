sudo ifconfig enp0s3 down
sudo ifconfig enp0s3 10.0.0.10/24
sudo ifconfig enp0s3 up
sudo route add default gw 10.0.0.1 enp0s3
route
ifconfig
