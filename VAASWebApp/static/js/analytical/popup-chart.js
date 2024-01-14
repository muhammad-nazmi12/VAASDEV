var popupButton = document.getElementById("popupButton");
var popup = document.getElementById("popup");
var closePopup = document.getElementById("closePopup");

popupButton.addEventListener("click", function(){
    popup.style.display="block";
});

closePopup.addEventListener("click",function(){
    popup.style.display="none";
});

window.addEventListener("click", function(event){
    if(event.target === popup){
        popup.style.display="none";
    }
});