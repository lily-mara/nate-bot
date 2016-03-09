import json
import logging

import tornado.httpclient as http

import settings

logger = logging.getLogger(__name__)


def handle_message_post(response):
	logger.info('%s', response)


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
