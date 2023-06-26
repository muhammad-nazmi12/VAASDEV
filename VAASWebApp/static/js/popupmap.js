//Define a function to retrieve and display the map data
function displayMap(){
    fetch('/map-data')
    .then(response=>response.json())
    .then(data=>{
        //Process the received data and display the map
        var centerpoint=[data.latitude,data.longitude];
        var mapElement = document.getElementById('popup-map');
        var mapDisplay =L.map(mapElement).setView(centerpoint,6);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
            attribution: 'Map data @ <a href="https://openstreetmap.org"> OpenStreetMap </a> contributors',
            maxZoom:18,
        }).addTo(mapDisplay);
    })
    .catch(error=>{
        console.error('Error: ', error);
    });
}

//Call the displayMap fnction to retrieve and display the map
displayMap();