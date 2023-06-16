function openNav(){
    document.getElementById("mySidenav").style.width="250px";
    document.getElementById("myCRDisplay").style.marginLeft="250px";
    document.getElementById("myCRDisplay1").style.width="1000px";
    document.getElementById("myCRDisplay2").style.width="1000px";
    document.getElementById("myCRListDisplay").style.width="975px";
    document.getElementById("myRDListDisplay").style.width="975px";
}

function closeNav(){
    document.getElementById("mySidenav").style.width="0";
    document.getElementById("myCRDisplay").style.marginLeft="0";
    document.getElementById("myCRDisplay1").style.width="1300px";
    document.getElementById("myCRDisplay2").style.width="1300px";
    document.getElementById("myCRListDisplay").style.width="1275px";
    document.getElementById("myRDListDisplay").style.width="1275px";
}

$(document).ready(function() {
  console.log("reportlib.js loaded"); 

  $('#createcase-popup').click(function() {
      openPopup('/create/');
  });

  $('#popup-close').click(function() {
      closePopup();
  });
});

function openPopup(url) {
  $('#popup-content').load(url);
  $('#popup').fadeIn();
}

function closePopup() {
  $('#popup').fadeOut();
}