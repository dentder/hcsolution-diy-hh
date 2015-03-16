# Introduction #

Creat a simple page using the NodeJS


# Details #


1. Create file hello.js in Ubuntu
```
    var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World. Hoang Hai Testing\n');
}).listen(1337, '192.168.0.115');
console.log('Server running at http://192.168.0.115:1337/');
```
2. copy file to board by

` scp hello.js root@192.168.0.115: `

3. login board

` ssh root@192.168.0.115 `

4. run file


` node hello.js `

5. Result: **Sucessfuly**

---- end of report ---
Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages