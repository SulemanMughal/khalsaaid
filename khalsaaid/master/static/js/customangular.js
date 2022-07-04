// JavaScript Document
app = angular.module('khalsaaidapp', ['ui.bootstrap']);

app.config(['$interpolateProvider', function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    }]);

app.filter('startFrom', function() {
    return function(input, start) {
        start = +start; //parse to int
        return input.slice(start);
    }
});

app.filter('limitHtml', function() {
    return function(text, limit) {

        var changedString = String(text).replace(/<[^>]+>/gm, '');
        var length = changedString.length;

        return changedString.length > limit ? changedString.substr(0, limit - 1) : changedString; 
    }
});
app.filter('htmlToPlaintext', function() {
    return function(text) {
      return  text ? String(text).replace(/<[^>]+>/gm, '').replace(/&nbsp;/gi,'') : '';
    };
  });

function setdocumentheight()
{
	var pagecontainer = $('.page-content').height();
	var docheight = $(document).height();
	
	if(pagecontainer < 650)
	{
		$('.page-content').css('min-height',docheight-241);
	}
	else
	{
		$('.page-content').css('min-height','auto');
	}
}

//check support value box press key is numeric or not.
function checknumber(e) {

    //if the letter is not digit then display error and don't type anything
    if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
        e.preventDefault();
        return false;
    } else {
        return true;
    }
}