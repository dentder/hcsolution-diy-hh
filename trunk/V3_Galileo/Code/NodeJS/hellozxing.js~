var qrdecoder = require('node-zxing')({ZXingLocation: "zxinglib"});
var path = "pdf417ex01.jpg";
qrdecoder.decode(path, 
  function(err, out) {
    console.log('Zxing hello world. Hoang Hai');
    console.log('Error:  '+err);
    console.log('Result:  '+out);
  }
);
