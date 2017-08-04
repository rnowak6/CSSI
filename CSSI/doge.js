function fade() {
  $("img").fadeOut();
  $( "#disappear").unbind( "click" );
  $("#disappear").click(fadeIn);

}

$(document).ready(function() { //indicates what is being used
    $("#disappear").click(fade);
    $("#bark").click(alerting);
    $("#age").click(dogYears);

  }
)

function fadeIn() {
  $("img").fadeIn();
  $( "#disappear").unbind( "click" );
  $("#disappear").click(fade);
}

function moveText() {
  var user_text = $('input').val();
  $('#result').text(user_text);
}

function alerting(){
  alert("You said: "+ $('input').val()+ "\nCosmo says: Woof!");
}

function dogYears() {
  var age=$('input').val()*5;
  $('#result').value(age);
}
