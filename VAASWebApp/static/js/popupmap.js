var centerpoint=[5.5341995,108.5584311];
var mapElement =document.getElementById("map2");

//Check if the map container already has an initialized map
if(mapElement && !mapElement._leaflet_id){
    var map = L.map("map2").setView(centerpoint,6);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>contributors',
        maxZoom: 18,
    }).addTo(map);
}