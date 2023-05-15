/*For sending HTML formatted text, use the "html" property instead
of the text property*/

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
  to: 'samuel_okoduwa@yahoo.com, samue_lokoduwa@outlook.com',
  subject: 'Sending Email using Node.js',
  html: '<h1>Welcome to NodeJs</h1><p>It was very easy!<p>'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});
