$(document).ready(function(){
	 
	 $('#contact-form').validate(
	 {
	  rules: {
		first_name: {
		  minlength: 2,
		  required: true
		},
		last_name: {
		  minlength: 2,
		  required: true
		},
		email: {
		  required: true,
		  email: true
		},
		mobile_phone: {
		  required: true,
		  digits: true,
		  minlength: 8,
		},
		year_start: {
		  required: true,
		  min: 1962,
		  digits: true
		},
		year_end: {
		  required: true,
		  min: 1963,
		  digits: true
		},
	  },
	  highlight: function(element) {
		$(element).closest('.control-group').removeClass('success').addClass('error');
	  },
	  success: function(element) {
		element
		.text('OK!').addClass('valid')
		.closest('.control-group').removeClass("error").addClass("succes");
	  }
	 });
	}); 

$(document).ready(function() 
		{ 
			$("#myTable").tablesorter( {sortList: [[0,0]]} ); 
		} 
	); 