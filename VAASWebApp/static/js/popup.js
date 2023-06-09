function nextForm(formNumber){
    //Hide the current form
    var currentForm = document.getElementById("form" + (formNumber-1));
    currentForm.style.display = "None";

    //Show the next form
    var nextForm = document.getElementById("form" + formNumber);
    nextForm.style.display = "block";
}

function addPersonField(){
    var entry = document.createElement("div");
    entry.setAttribute("id","person_entry");
    entry.innerHTML = 
    '<label for="person_name">Name: </label>'+
    '<input type="text" id="person_name" name="person_name">'+
    '<br>'+
    '<label for="person_age">Age: </label>'+
    '<input type="number" id="person_age" name="person_age">'+
    '<br>'+
    '<label for="person_gender">Gender: </label>'+
    '<select id="person_gender" name="person_gender">'+
    '   <option value=""></option>'+
    '   <option value="male">Male</option>'+
    '   <option value="female">Female</option>'+
    '</select>'+
    '<br>'+
    '<label for="driver_license">License: </label>'+
    '<input type="text" id="driver_license" name="driver_license">'+
    '<br>'+
    '<label for="injuries">Injuries: </label>'+
    '<textarea id="injuries" name="injuries"></textarea>'+
    '<br>';
    document.getElementById("person_fields").appendChild(entry);
}

function addVehicleField(){
    var entry = document.createElement("div");
    entry.setAttribute("id","vehicle_entry");
    entry.innerHTML=
    '<label for="vehicle_model">Vehicle Model: </label>'+
    '<input type="text" id="vehicle_model" name="vehicle_model">'+
    '<br>'+
    '<label for ="vehicle_type">Vehicle Type: </label>'+
    '<select id="vehicle_type" name="vehicle_type">'+
        '<option value=""></option>'+
        '<option value="car">Car</option>'+
        '<option value="truck">Truck</option>'+
        '<option value="motorcycle">Motorcycle</option>'+
        '<option value="bicycle">Bicycle</option>'+
    '</select>'+
    '<br>'+
    '<label for="plate_number">Plate Number: </label>'+
    '<input type="text" id="plate_number" name="plate_number">'+
    '<br>'+
    '<label for="vehicle_owner">Owner: </label>'+
    '<input type="text" id="vehicle_owner" name="vehicle_owner">'+
    '<br>'+
    '<label for="vehicle_damage">Damages: </label>'+
    '<textarea id="vehicle_damage" name="vehicle_damage"></textarea>'+
    '<br>';
    document.getElementById("vehicle_fields").appendChild(entry);
}

function addReferenceField(){
    var entry = document.createElement("div");
    entry.setAttribute("id","reference_entry");
    entry.innerHTML=
        '<label for="ref_item">Reference Item: </label>'+
        '<input type="file" id="ref_item" name="ref_item">'+
        '<br>'+
        '<label for="owned_by">Owned By: </label>'+
        '<input type="text" id="owned_by" name="owned_by">'+
        '<br>'+
        '<label for="ref_type">Type: </label>'+
        '<select id="ref_type" name="ref_type">'+
            '<option value=""></option>'+
            '<option value="document">Document</option>'+
            '<option value="image">Image</option>'+
            '<option value="video">Video</option>'+
        '</select>'+
        '<br>';
        document.getElementById("reference_fields").appendChild(entry);
}

var centerpoint=[5.5341995,108.5584311];
var map = L.map('map2').setView(centerPoint,6);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>contributors',
    maxZoom: 18,
}).addTo(map);
