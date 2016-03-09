import logging

import tornado.web as web

logger = logging.getLogger(__name__)


class MessageHandler(web.RequestHandler):
	def post(self):
		logger.info('Got message %s', self.request.body)
