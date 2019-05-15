import sys



sys.path.append('/var/www/cit/test_bed_environment/lib/python3.6/site-packages')#this line for Ubuntu 18.04
sys.path.append('/var/www/cit/test_bed_environment/lib/python3.5/site-packages')#this line for Ubuntu 16.04
sys.path.append('/var/www/cit')

from CIT_API import app as application
