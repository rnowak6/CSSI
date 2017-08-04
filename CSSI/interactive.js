function disappear() { //tells us what we are trying to hide
  $("#title").toggleClass("hidden");
}

function hideOLs() {
  $("ol").hide();
}

$(document).ready(hideOLs);

$(document).ready(function() { //indicates what is being used to disappear
    $("#disappear-div").click(disappear);
    $("#showText").click(alerting);

  }
)

function alerting(){
  alert($('input').val());
}

function toggleOLs() {
  $("ol").toggle();
}

function timeClock() {
  setTimeout(alerting,3000);
  $("img").click(toggleOLs);
}
function fades() {
  $("img").fadeOut();
}

$(document).ready(fades);


function moveText() {
  var user_text = $('input').val();
  $('#result').text(user_text);
}
