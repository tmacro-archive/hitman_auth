#!/usr/bin/python3
import sys
import socket
from hitman.util.config import config
from hitman.util.log import getLogger
import time
from hitman.app import db
from hitman.models import User
from sqlalchemy_utils import database_exists, create_database

_log = getLogger(__name__)

def check_server(address, port):
	# Create a TCP socket
	s = socket.socket()
	_log.info("Attempting to connect to %s on port %s"%(address, port))
	try:
		s.connect((address, port))
		_log.info("Connected to %s on port %s"%(address, port))
		return True
	except socket.error as e:
		_log.error("Connection to %s on port %s failed: %s"%(address, port, e))
		return False

if __name__ == '__main__':
	for x in range(10):
		if check_server('postgres', 5432):
			if not database_exists(db.engine.url):
				_log.info('Database does not exist, creating...')
				create_database(db.engine.url)
				db.create_all()
				_log.debug('Finished creating database')
			else:
				_log.info('Database already exists')
			sys.exit(0)
		else:
			_log.error('Failed to connect to database. Failures: %i'%(x+1))
			time.sleep(5)
	sys.exit(1)