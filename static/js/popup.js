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