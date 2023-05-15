//The file system module methods of creting new files

//=> creating file using the appendFile() method
var fs = require('fs');

fs.appendFile('mynewfile1.txt', 'Hello content!', function (err) {
	if (err) throw err;
	console.log('Saved!');
});

//=> creating a new empty file using the open() method
var fs = require('fs');
fs.open('mynewfile2.txt', 'w', function(err, file){
	if (err) throw err;
	console.log('Saved!')
})

//=> creating a file using the writeFile() method
var fs = require('fs');

fs.writeFile('mynewfile3.txt', 'Hello Content', function(err){
	if (err) throw err;
	console.log('Saved!');
})