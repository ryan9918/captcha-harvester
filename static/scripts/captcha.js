$(function (){
	
	var $tokens = $('#tokens');

	$.ajax({
		type: 'GET',
		url: '/api/count',
		success: function(data) {
			$tokens.text("Available Tokens: " + data.count)
		}
	});

});

setInterval(function (){
	
	var $tokens = $('#tokens');

	$.ajax({
		type: 'GET',
		url: '/api/count',
		success: function(data) {
			$tokens.text("Available Tokens: " + data.count)
		}
	});

}, 5000);