sudo ifconfig enp0s3 down
sudo ifconfig enp0s3 129.108.7.29/24
sudo ifconfig enp0s3 up
sudo route add default gw 129.108.7.1 enp0s3
route
ifconfig
