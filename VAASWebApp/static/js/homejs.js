function openNav(){
    document.getElementById("mySidenav").style.width="150px";
    document.getElementById("myHome").style.marginLeft="100px";
    document.getElementById("myHomeContent").style.width="1300px";
    document.getElementById("myOMDisplay").style.width="300px";
    document.getElementById("myDUDisplay").style.width="1275px";
}

function closeNav(){
    document.getElementById("mySidenav").style.width="0";
    document.getElementById("myHome").style.marginLeft="0";
    document.getElementById("myHomeContent").style.width="1300px";
    document.getElementById("myOMDisplay").style.width="300px";
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