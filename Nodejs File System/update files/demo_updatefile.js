//The fs.appendFile() method. This appends the specified content 
//at the end of a speified file

var fs = require('fs');

fs.appendFile('mynewFile1.txt', 'This is my text.', function(err){
	if (err) throw err;
	console.log('Updated!');
});


//The fs.writeFile() method replaces the specified file and content:
var fs = require('fs')

fs.writeFile('mynewfile3.txt', 'This is my text', function(err){
	if (err) throw err
	console.log('Replaced!');
});