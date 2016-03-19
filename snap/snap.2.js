var page = require('webpage').create();
var args = require('system').args;

var pageW = 1024;
var pageH = 768;

page.viewportSize = {
  	width: pageW,
	height: pageH
};


var url =  args[1];
var filename = args[2];


page.open(url, function (status) {
    if (status !== 'success')
    {
        console.log('Unable to load ' + url + ' !');
        phantom.exit();
    } 
    else 
    { 
	    window.setTimeout(function () {
            page.clipRect = { left: 0, top: 0, width: pageW, height: pageH };
            page.render(filename);
            console.log('finish:', filename);
            phantom.exit();
            }, 1000);
    }
});


