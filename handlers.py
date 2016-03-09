import json
import logging

import tornado.web as web

import settings
from groupme import post_message

logger = logging.getLogger(__name__)


def tell_nate_he_had_a_good_point():
	post_message("That's a great point, Nate!")


class MessageHandler(web.RequestHandler):
	def post(self):
		body = json.loads(self.request.body)

		if body['user_id'] in settings.NATE_ID:
			tell_nate_he_had_a_good_point()
			logger.info('Telling Nate that he had a good point')

		self.finish('ok')
