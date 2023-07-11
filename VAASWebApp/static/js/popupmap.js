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
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>contributors',
            maxZoom: 18,
        }).addTo(mapDisplay);

        var marker;

        //Add a "mousedown" event listener to the map
        mapDisplay.on('mousedown',function(e){
            if(!marker){
                marker=L.marker(e.latlng,{draggable:true}).addTo(mapDisplay);
                }
        });

        //Add a "mouseup" event listener to the map
        mapDisplay.on('mouseup',function(e){
            if(marker){
                document.getElementById('location_longcoord').value=marker.getLatLng().lng;
                document.getElementById('location_latcoord').value=marker.getLatLng().lat;
            }
        });

        // Add a "dragend" event listener to the marker
        mapDisplay.on('dragend',function(e){
            if(marker){
                document.getElementById('location_longcoord').value=marker.getLatLng().lng;
                document.getElementById('location_latcoord').value=marker.getLatLng().lat;
            }
        });

        //Add a "mousemove" event listener to the map
        //mapDisplay.on('mousemove',function(e){
        //    if(marker){
        //        marker.setLatlng(e.latlng);
        //    }
        //});

        //Add a "mouseup" event listener to the map
        //mapDisplay.on('mouseup',function(e){
       //     if(marker){
       //        marker.setLatlng(e.latlng);
       //         document.getElementById('location_longcoord').value=marker.getLatLng().lng;
       //         document.getElementById('location_latcoord').value=marker.getLatLng().lat;
       //     }
        //});

        

        //mapDisplay.on('click',function(e){
        //    var latitude = e.latlng.lat;
        //    var longtitude = e.latlng.lng;
        //    var marker = L.marker([latitude,longtitude]).addTo(mapDisplay);
        //    document.getElementById('location_longcoord').value=longtitude;
        //    document.getElementById('location_latcoord').value=latitude;
        //});
    })
    .catch(error=>{
        console.error('Error: ', error);
    });
}

//Call the displayMap fnction to retrieve and display the map
displayMap();