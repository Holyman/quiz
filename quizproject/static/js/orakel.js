

// <!--  OOOOOO  00000   000000  0000
//       OO  00  00  00  00      0000
//       OO  00  00000     00     00
//       OO  00  00  00      00
//       OOOOOO  00000   000000   00  -->
// <!-- AH, DEN VAR SVETT! -->
// <!-- OBS!OBS! HER SETTES DATOEN FOR LANSERING! -->

// <!-- Script som bestemmer hvilken boks som vises -->


// Sett inn dato her, bruk engelsk på formen July 30, 2013 14:00:00
var expiry  = new Date("July 30, 2013 14:40:00")

window.setInterval(function(){

  var current = new Date();

  if(current.getTime()>expiry.getTime()){
    $('#open').show();
    $('#not_open').hide();
  } else {
    $('#not_open').show();
    $('#open').hide();
  }
}, 100);

