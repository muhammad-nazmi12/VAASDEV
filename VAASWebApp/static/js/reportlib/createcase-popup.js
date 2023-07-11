function nextForm(formNumber){
    //Hide the current form
    var currentForm = document.getElementById("form" + (formNumber-1));
    currentForm.style.display = "None";

    //Show the next form
    var nextForm = document.getElementById("form" + formNumber);
    nextForm.style.display = "block";
}

function previousForm(formNumber){
    //Hide the current form
    var currentForm = document.getElementById("form" + (formNumber+1));
    currentForm.style.display = "None";

    //SHow the previous form
    var previousForm = document.getElementById("form" + formNumber);
    previousForm.style.display = "block";
}

function addPersonField(){
    var entry = document.createElement("div");
    entry.setAttribute("id","person_entry");
    entry.innerHTML = 
    '<label for="person_name">Name: </label>'+
    '<input type="text" id="person_name" name="person_name" onchange="updateVehicleOwnerOptions()">'+
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
    '<label for="person_type">Type: </label>'+
    '<select id="person_type" name="person_type">'+
    '   <option value=""></option>'+
    '   <option value="Driver">Driver</option>'+
    '   <option value="Biker">Biker</option>'+
    '   <option value="Passenger">Passenger</option>'+
    '</select>'+
    '<br>'+
    '<label for="driver_license">License: </label>'+
    '<input type="text" id="driver_license" name="driver_license">'+
    '<br>'+
    '<label for="injury_level">Injury Level: </label>'+
    '<select id="injury_level" name="injury_level">'+
    '    <option value=""></option>'+
    '    <option value="Minor">Minor</option>'+
    '    <option value="Moderate">Moderate</option>'+
    '    <option value="Severe">Severe</option>'+
    '</select>'+
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
    '<select id="vehicle_owner" name="vehicle_owner">'+
    '<option value=""></option>'+
    '</select>'+
    '<br>'+
    '<label for="damage_level">Damage Level: </label>'+
    '<select id="damage_level" name="damage_level">'+
    '   <option value=""></option>'+
    '    <option value="Minor">Minor</option>'+
    '    <option value="Major">Major</option>'+
    '</select>'+
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
        '<input type="file" id="ref_item" name="ref_items[]" multiple>'+
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

function updateVehicleOwnerOptions(){
    var personNames = document.querySelectorAll("#person_fields input[name='person_name']");
    var vehicleOwnerDropdown = document.getElementById("vehicle_owner");

    //Clear existing options
    vehicleOwnerDropdown.innerHTML = '<option value=""></option>';

    //Add person names as options
    for(var i=0;i<personNames.length;i++){
        var personName = personNames[i].value;
        if(personName.trim()!==''){
            var option=document.createElement('option');
            option.value=personName;
            option.textContent=personName;
            vehicleOwnerDropdown.appendChild(option);
        }
    }
}

function previewReference(input){
    var previewContainer = document.getElementById("reference_preview");
    var file=input.files[0];

    if(file){
        var reader=new FileReader();

        reader.onload = function(e){
            var preview = document.createElement("div");
            preview.innerHTML="Preview: " + file.name;
            previewContainer.innerHTML="";
            previewContainer.appendChild(preview);
        }

        reader.readAsDataURL(file);
    }else{
        previewContainer.innerHTML="";
    }
}
