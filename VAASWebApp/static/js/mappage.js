function openNav(){
    document.getElementById("mySidenav").style.width="250px";
    document.getElementById("myMap").style.marginLeft="200px";
    document.getElementById("myMapView").style.width="955px";
    document.getElementById("myMapDisplay").style.width="865px";
    document.getElementById("myMDMenu").style.marginLeft="50px";
}

function closeNav(){
    document.getElementById("mySidenav").style.width="0";
    document.getElementById("myMap").style.marginLeft="0";
    document.getElementById("myMapView").style.width="1105px";
    document.getElementById("myMapDisplay").style.width="1015px";
    document.getElementById("myMDMenu").style.marginLeft="0";
}

function OCMapMenu(){
    var MDM = document.getElementById("myMDMenu");
    if (MDM.style.width === "0px" || MDM.style.width === "") {
      MDM.style.width = "210px";
    } else {
      MDM.style.width = "0px";
    }
}

function CoorMenuBtn(){
  var CM = document.getElementById("myCoorMenu");
  if(CM.style.width ==="0px" || CM.style.width===""){
    CM.style.width="100px";
    CM.style.height="200px";
  }else{
    CM.style.width="0px";
    CM.style.height="0px";
  }
}


