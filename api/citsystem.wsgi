import sys

#activate_this = '/var/www/cit/__init__.py'
#with open(activate_this) as file:
#  exec(file_.read(), dict(__init__=activate_this))

sys.path.append('/var/www/cit/test_bed_environment/lib/python3.6/site-packages')#this line for Ubuntu 18.04
sys.path.append('/var/www/cit/test_bed_environment/lib/python3.5/site-packages')#this line for Ubuntu 16.04
sys.path.append('/var/www/cit')

#from app import app as application
from CIT_API import app as application
