function stuffToDoWhenFadeOutisDone(){
  alert("done fading out")
}

function stuffToDoWhenClicked(){
  $("#hello").fadeOut(1000);

}

function stuffToDoWhenReady(){
$("#hello").fadeOut(1000, stuffToDoWhenFadeOutisDone);
//$("#emoji").click(stuffToDoWhenClicked)
$("#emoji").click(function(){
  $("#emoji").fadeOut(1000);
})
}

$(document).ready(stuffToDoWhenReady)
