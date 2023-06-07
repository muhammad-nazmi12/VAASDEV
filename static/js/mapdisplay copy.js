var centerPoint = JSON.parse(document.getElementById('center-point').textContent);

var map = L.map('myMapDisplay').setView(centerPoint,6);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>contributors',
    maxZoom: 19,
    tileSize:512,
    zoomOffset:-1
}).addTo(map);

var markerIcon=L.icon({
    iconUrl:"/static/images/marker.png",
    iconSize:[25,41],
    iconAnchor:[12,41]
});

var marker = L.marker(centerPoint,{icon:markerIcon}).addTo(map);