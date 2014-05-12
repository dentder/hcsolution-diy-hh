/*
 * App to create web for Galileo
 * Hoang Hai version 1.0
 */
var express = require('express') // us
  , stylus = require('stylus')
  , nib = require('nib')

  //var sys = require('sys')
  var exec = require('child_process').exec;
  var child;
  var fs = require('fs');
  var app = express() 
  var multer  = require('multer')



function compile(str, path) {
  return stylus(str)
    .set('filename', path)
    .use(nib())
}
app.set('views', __dirname + '/views')
app.set('view engine', 'jade')
app.use(express.logger('dev'))
app.use(stylus.middleware(
  { src: __dirname + '/public'
  , compile: compile
  }
))
app.use(multer({
        dest: './public/uploads/',
        rename: function (fieldname, filename) {
            return filename.replace(/\W+/g, '-').toLowerCase();
        }
    }));
app.use(express.static(__dirname + '/public'))



app.get('/', function (req, res) {
  res.render('default',
  { title : 'Mini Demix Module - Galileo Contest - MDO HVE VN' }
  )
})


app.get('/upload', function (req, res) {
  res.render('Upload',
  { title : 'Upload VIDs list' }
  )
})

app.post('/upload', function(req, res) {
  console.log('log: POST Upload : ')
  console.log(req.body)
  console.log('log: req.files.displayImage.path: ' + req.files.displayImage.path );
  console.log('log: req.files.displayImage.name: ' + req.files.displayImage.name );
  /*
  fs.readFile(req.files.displayImage.path, function (err, data) {
 
    var newPath = __dirname + "/uploads/"+req.files.displayImage.name;
    console.log('newPath = '+ newPath);
    fs.writeFile(newPath, data, function (err) {
      if (err) throw err;
      res.redirect("back");
      console.log('File upload is done');
    });
  });
  */
 // res.redirect("back");  // TODO: send to user upload done- DONE
 res.render('message',
  { message: 'File ' + req.files.displayImage.name + ' is uploaded suscessfully to '+req.files.displayImage.path + '.' }  
  )
});

//-----------------------------------------------------
app.get('/checkcamera', function (req, res) {
  console.log("Checking camera readiness: gphoto2 --auto-detect")
//gphoto2 --auto-detect

   child = exec("gphoto2 --auto-detect", function (error, stdout, stderr) {
	//  sys.print('stdout: ' + stdout);
	//  sys.print('stderr: ' + stderr);
            console.log('stdout: ' + stdout);
            console.log('stderr: ' + stderr);

	  if (error !== null) 
          {
	    console.log('exec error: ' + error);
            res.render('message',
  		{ message: 'ERROR EXEC | checking camera | ' + error }  
  		    )
	  }   
	  else
	  {
  		res.render('message',
  		{ message: 'SUCESSFUL EXEC|checking camera | ' + stdout }  
  		)
          }
          })
  })
//-----------------------------------------------------
app.get('/takepicture', function (req, res) {
  console.log("taking camera picture")
  //gphoto2 --auto-detect

   child = exec("gphoto2 --capture-image-and-download", function (error, stdout, stderr) {
	//  sys.print('stdout: ' + stdout);
	//  sys.print('stderr: ' + stderr);
            console.log('stdout: ' + stdout);
            console.log('stderr: ' + stderr);

	  if (error !== null) 
          {
	    console.log('exec error: ' + error);
            res.render('message',
  		{ message: 'ERROR EXEC | taking camera |' + error }  
  		    )
	  }   
	  else
	  {
  		res.render('message',
  		{ message: 'SUCESSFUL EXEC |taking camera | ' + stdout }  
  		)
          }
          })
  })
//-----------------------------------------------------  
app.get('/processpicture', function (req, res) {
       console.log("Processing picture")
        //  excutes taking picture

      // res.render('message',
  	//	{ message: 'Status of image taking....DONE' }   )
	// executes image processing
	child = exec("python readrecipe.py", function (error, stdout, stderr) {
	//  sys.print('stdout: ' + stdout);
	//  sys.print('stderr: ' + stderr);
            console.log('stdout: ' + stdout);
            console.log('stderr: ' + stderr);

	  if (error !== null) 
          {
	    console.log('exec error: ' + error);
            res.render('message',
  		{ message: 'Status of image processing: exec error: ' + error }  
  		    )
	  }   
    

	})

  res.render('result2',
  { title : 'Mini Demix Module - Galileo Contest - MDO HVE VN' }
  )
  
})

app.listen(8080)
console.log("App run at localhost:8080")
