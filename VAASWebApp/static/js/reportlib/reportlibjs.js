function openNav(){
    document.getElementById("mySidenav").style.width="150px";
    document.getElementById("myCRDisplay").style.marginLeft="50px";
    document.getElementById("myCRDisplay1").style.width="1300px";
    document.getElementById("myCRDisplay2").style.width="1300px";
    document.getElementById("myCRListDisplay").style.width="1275px";
    document.getElementById("myRDListDisplay").style.width="1275px";
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
      openCCPopup('/create/');
  });

  $('#popup-close').click(function() {
      closeCCPopup();
  });
});

function openCCPopup(url) {
  $('#case-popup-content').load(url);
  $('#create-case-popup').fadeIn();
}

function closeCCPopup() {
  $('#create-case-popup').fadeOut();
}