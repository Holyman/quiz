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
    .closest('.control-group').removeClass('error').addClass('success');
    }
   });
  }); 


$(document).ready(function() {
  var deck = new $.scrolldeck({
    buttons: '.nav-button',
    slides: '.slide',
    duration: 600,
    easing: 'easeInOutExpo',
	offset: 0
  });

    $("#myTable").tablesorter( {sortList: [[0,0]]} ); 

      resetForm($('#contact-form')); // by id, recommended


		
 $("#info_text textarea").attr('placeholder', 'Har du allergier eller lignende kan du skrive det her...'); 


	// function checkAvailableHeight(){
	//     // var holder_slide1 = document.getElementById("holder_slide1");
	//     // holder_slide1.style.marginTop = (((window.innerHeight - 772) / 2)) + "px";

	//     // var holder_slide2 = document.getElementById("holder_slide2");
	//     // holder_slide2.style.marginTop = (((window.innerHeight - 475) / 2)) + "px";

	//     // var holder_slide3 = document.getElementById("holder_slide3");
	//     // //  var  = $('myTable').css("height");
	//     //   var height_table = document.getElementById('myTable').offsetHeight; 
	//     // //  alert(height_table)


	//     // holder_slide3.style.marginTop = (((window.innerHeight - height_table) / 2)) + "px";
	// }
		

    function abso() {

        $('#holder_slide').css({
            // position: '',
            // width: $(window).width(),
            height: $(window).height(),
            //top: '',
        });

    }






    $(window).resize(function() {
        abso();
        // checkAvailableHeight(); 
   

	 //  var deck = new $.scrolldeck({
	 //    buttons: '.nav-button',
	 //    slides: '.slide',
	 //    duration: 600,
	 //    easing: 'easeInOutExpo',
		// offset: 0
		//  });

	 //    abso();
  //       checkAvailableHeight();

    });
	 //window.onload = checkAvailableHeight();

	 abso();




});


function resetForm($form) {
    $form.find('input:text, input:password, input:file, select, textarea').val('');
    $form.find('input:radio, select')
         .removeAttr('checked').removeAttr('selected');
    $form.find('select').val('');

}



  $(".nav li a").on("click", function( e ) {
    $("li").removeClass("active");
    $( e.target ).closest("li").addClass("active");

  });

  $(".jumbotron a").on("click", function( e ) {
    $(".top-menu li").removeClass("active");
    $(".meld").closest("li").addClass("active");

  });

  $('#linje_modal').on('hidden', function () {
    $(".top-menu li").removeClass("active");
  })


	//$(window).resize(); 

