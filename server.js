var http = require('http'),
	winston = require('winston');

const GROUPME_TOKEN = process.env.GROUPME_TOKEN;
const BOT_ID = process.env.BOT_ID;
const NATE_ID = process.env.NATE_ID;

function postMessage(botId, text, callback) {
	var postData = JSON.stringify({
		bot_id: botId,
		text: text,
	});

	var postOptions = {
		host: 'api.groupme.com',
		port: '443',
		path: '/v3/bots/post',
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'Content-Length': Buffer.byteLength(postData)
		}
	};

	var post = http.request(postOptions, function(res) {
		var data = '';
		res.setEncoding('utf8');

		res.on('data', function (chunk) {
			data += chunk;
		});

		res.on('end', function () {
			winston.info(data);
			callback(data);
		});
	});

	post.write(postData);
	post.end();
}

function tellNateHeHadAGoodPoint() {
	postMessage(
		BOT_ID,
		"That's a great point Nate!",
		function (d) {
			winston.info('Told Nate that he had a great point, got', d);
		});
}

/**
 * Creates the server for the pinpoint web service
 * @param {int} port: Port for the server to run on
 */
exports.createServer = function (port) {
	var server = http.createServer(function (request, response) {
		var data = '';

		winston.info('Incoming Request', { url: request.url });

		request.on('data', function (chunk) {
			data += chunk;
		});

		request.on('end', function () {
			var parsed = JSON.parse(data);

			if (parsed.user_id == NATE_ID) {
				winston.info('Saw message from Nate, telling him that it was a good point.');
				tellNateHeHadAGoodPoint();
			}
		});

		response.writeHead(501, { 'Content-Type': 'application/json' });
		response.end(JSON.stringify({ message: 'not implemented' }));
	});

	if (port) {
		server.listen(port);
		winston.info('Listening on port ' + port);
	}

	return server;

};
