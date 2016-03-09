import json
import logging

import tornado.web as web

import settings
from groupme import post_message

logger = logging.getLogger(__name__)


class MessageHandler(web.RequestHandler):
	def post(self):
		body = json.loads(self.request.body.decode('utf-8'))

		if body['user_id'] in settings.NATE_ID:
			logger.info('Telling Nate that he had a good point')
			post_message("That's a great point, Nate!")
		else:
			logger.info('Some dummy just posted.')

		self.finish('ok')
