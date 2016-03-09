require('dotenv').config();
var serverLib = require('./server.js');

var server = serverLib.createServer(8080);
