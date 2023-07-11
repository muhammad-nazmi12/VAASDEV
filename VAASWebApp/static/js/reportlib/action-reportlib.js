function toggleCRPopup(popupId){
    var popupContent = document.getElementById(popupId);

    if(popupContent.style.display==='block'){
        popupContent.style.display = 'none';
    }else{
        popupContent.style.display='block';
    }
}

function toggleRefPopup(popupId){
    var popupContent = document.getElementById(popupId);

    if(popupContent.style.display==='block'){
        popupContent.style.display='none';
    }else{
        popupContent.style.display='block';
    }
}

function openCRPopup(popupId){
    var popup = document.getElementById(popupId);
    var popupContent= popup.querySelector('.CR-popup-content');

    popupContent.style.display = 'block';

    window.onclick = function(event){
        if(event.target !== popupContent && !popupContent.contains(event.target)){
            popupContent.style.display='none';
        }
    };
}

function openRefPopup(popupId){
    var popup = document.getElementById(popupId);
    var popupContent= popup.querySelector('.RD-popup-content');

    popupContent.style.display = 'block';

    window.onclick = function(event){
        if(event.target !== popupContent && !popupContent.contains(event.target)){
            popupContent.style.display='none';
        }
    };
}

function handleCaseChange(popupId,selectedOption){
    var popupContent = document.getElementById(popupId);
    //Hide the popup content after an action is selected
    popupContent.style.display='none';

    //Handle the selected action
    if(selectedOption === 'View'){
        //Perform the view action
        console.log('Performing View action for CaseID: ' + popupId);
    }else if(selectedOption==='Edit'){
        //Perform the edit action
        console.log('Perforoming Edit action for CaseID: ' + popupId);
    }else if(selectedOption==='Delete'){
        //Perform the delete action
        console.log('Performing Delete action for CaseID: ' + popupId);
    }
}

function handleRefChange(popupId,selectedOption){
    var popupContent = document.getElementById(popupId);
    //Hide the popup content after an action is selected
    popupContent.style.display='none';

    //Handle the selected action
    if(selectedOption === 'View'){
        //Perform the view action
        console.log('Performing View action for RefID: ' + popupId);
    }else if(selectedOption==='Delete'){
        //Perform the delete action
        console.log('Performing Delete action for RefID: ' + popupId);
    }
}