var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World. Hoang Hai Testing\n');
}).listen(1337, '192.168.0.115');
console.log('Server running at http://192.168.0.115:1337/');

