import sys

#activate_this = '/var/www/cit/__init__.py'
#with open(activate_this) as file:
#  exec(file_.read(), dict(__init__=activate_this))

#sys.path.append('/var/www/cit/test_bed_environment/lib/python3.5/site-packages')
sys.path.append('/var/www/cit')

from CIT_API import app as application
