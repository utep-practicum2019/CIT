import sys

#activate_this = '/var/www/cit/__init__.py'
#with open(activate_this) as file:
#  exec(file_.read(), dict(__init__=activate_this))

sys.path.append('/var/www/cit/test/lib/python3.5/site-packages')

from __init__ import app as application
