//Sending a mail
var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'samuelokoduwaosose@gmail.com',
    pass: 'sompto654@'
  }
});

var mailOptions = {
  from: 'samuelokoduwaosose@gmail.com',
  to: 'samuel_okoduwa@yahoo.com', 
  subject: 'Sending Email using Node.js',
  text: 'That was easy!'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});



