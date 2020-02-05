#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/luigi/")
sys.path.insert(0,"/var/www/luigi/luigi/")

import logging
logging.basicConfig(stream=sys.stderr)

from luigi import app as application
