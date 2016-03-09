import os
import logging.config


def get_bool(key):
	return os.environ.get(key, 'true').lower().strip() == 'true'


def get_int(key):
	return int(os.environ[key])


def get_str(key):
	return os.environ[key]


def get_list(key):
	return os.environ[key].split(',')


DEBUG = get_bool('debug')
GROUPME_TOKEN = get_str('GROUPME_TOKEN')
BOT_ID = get_str('BOT_ID')
NATE_ID = get_list('NATE_ID')

SETTINGS = {
	'debug': DEBUG,
}


logging.config.dictConfig({
	'version': 1,
	'handlers': {
		'console': {
			'class': 'logging.StreamHandler',
			'level': 'INFO',
			'stream': 'ext://sys.stdout',
		},
	},
	'formatters': {
		'default': {
			'format': '%(asctime)s %(levelname)-8s %(name)-15s %(message)s',
			'datefmt': '%Y-%m-%d %H:%M:%S',
		},
	},
})
