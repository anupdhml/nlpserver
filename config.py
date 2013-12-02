#!/usr/bin/env python

import logging

# Flask app debug value. 
#DEBUG = False # DEBUG AND INFO log levels won't be shown..
DEBUG = True 

# Used for running the flask server independent of mod_wsgi
#SERVERNAME = "127.0.0.1"
SERVERNAME = "localhost" # using SERVER_NAME makes views fail..
SERVER_PORT = 8139
#SERVER_PORT = 5000

# URLs from which request (ajax) can be made to this server
ALLOWED_DOMAINS = "*"                 # all
#ALLOWED_DOMAINS = "http://"+SERVERNAME # allow calls from elsewhere in the same server

#PREFERRED_URL_SCHEME='https'

LOG_FILE = "nlpserver.log" # If mod_wsgi is used, apache handles the log file..
DEFAULT_LOG_FORMATTER = logging.Formatter(\
   "%(asctime)s - %(levelname)s - %(message)s")
#DEFAULT_LOG_LEVEL = logging.DEBUG # not really needed since DEBUG_VAL above influences this
#DEFAULT_LOG_LEVEL = logging.WARNING
