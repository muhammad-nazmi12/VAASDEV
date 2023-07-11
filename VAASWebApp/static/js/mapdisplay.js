//var centerPoint = JSON.parse(document.getElementById('center-point').textContent);

//var map = L.map('myMapDisplay').setView(centerPoint,6);
var centerPoint=[5.5351995,108.5584311];
var map = L.map('myMapDisplay').setView(centerPoint,6);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>contributors',
    maxZoom: 18,
}).addTo(map);

var longdisplay = document.getElementById('LongCoorValue');
var latdisplay = document.getElementById('LatCoorValue');

map.on('moveend',function(e){
    var center = map.getCenter();
    var longtitude = center.lng;
    var latitude = center.lat;
    
    //Update coordinates display
    longdisplay.value=longtitude;
    latdisplay.value=latitude;
});

function CntrMarker(){
    map.setView(centerPoint,6);
}

//Retrieve the coordinates and address from the server-side
var dataPoints = JSON.parse('{{ data_points | escapejs }}');

dataPoints.forEach(function (data){
   var latitude = data.CoordLat;
   var longitude = data.CoordLong;

   var marker = L.marker([latitude,longitude]).addTo(map);
});



