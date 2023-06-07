var map = L.map('mapView').setView([5.1851749,104.3396811],6);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
                attribution:'Map data &copy; <a href="https://www.openstreetmap.org/"> OpenStreetMap </a> contributors',
                maxZoom:18,
            }).addTo(map);