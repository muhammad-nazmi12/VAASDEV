function openNav(){
    document.getElementById("mySidenav").style.width="250px";
    document.getElementById("myHome").style.marginLeft="250px";
    document.getElementById("myHomeContent").style.width="1000px";
    document.getElementById("myOMDisplay").style.width="155px";
    document.getElementById("myDUDisplay").style.width="975px";
}

function closeNav(){
    document.getElementById("mySidenav").style.width="0";
    document.getElementById("myHome").style.marginLeft="0";
    document.getElementById("myHomeContent").style.width="1300px";
    document.getElementById("myOMDisplay").style.width="455px";
    document.getElementById("myDUDisplay").style.width="1275px";
}

function updateClock(){
    var d = new Date();
    var time = d.toLocaleDateString();

    //replace the element with id "clock" with the updated time
    document.getElemenyById("clock").innerHTML = time;
}

//Update the clock every second
setInterval(updateClock, 1000);