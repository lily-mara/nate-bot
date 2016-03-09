import json
import logging

import tornado.httpclient as http

import settings

logger = logging.getLogger(__name__)


def url(*args):
	return 'https://api.groupme.com/v3' + ''.join(args) + '?token=' + settings.GROUPME_TOKEN


def handle_message_post(response):
	if response.code != 202:
		logger.error(
			'Error posting message! Got code %s: %s',
			response.code,
			response.reason,
		)


def post_message(text):
	request = http.HTTPRequest(
		'https://api.groupme.com/v3/bots/post',
		method='POST',
		body=json.dumps({
			'bot_id': settings.BOT_ID,
			'text': text,
		}),
		headers={
			'Content-Type': 'application/json',
		},
	)

	client = http.AsyncHTTPClient()
	client.fetch(request, callback=handle_message_post, raise_error=False)


def get_group_name(group_id):
	def handle_group_name(response):
		if response.code == 200:
			body = json.loads(response.body.decode('utf-8'))
			logger.info(
				'Running bot in group "%s"',
				body['response']['name'],
			)
		else:
			logger.error(
				'There is no group with id %s',
				group_id,
			)

	client = http.AsyncHTTPClient()
	client.fetch(
		url('/groups/', group_id),
		callback=handle_group_name,
		raise_error=False
	)


def get_bot_group(bot_id):
	def handle_bot_group(response):
		if response.code == 200:
			body = json.loads(response.body.decode('utf-8'))
			bot = [i for i in body['response'] if i['bot_id'] == bot_id][0]
			get_group_name(bot['group_id'])
		else:
			logger.error(
				'There is no bot with id %s',
				bot_id,
			)

	client = http.AsyncHTTPClient()
	client.fetch(
		url('/bots'),
		callback=handle_bot_group,
		raise_error=False
	)
