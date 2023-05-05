document.addEventListener("DOMContentLoaded", () => {
    var pictures = document.querySelectorAll("#id_pictures");
    pictures.forEach(picture => {
        picture.addEventListener("change", duplicate_picture());
        
    })
})

function duplicate_picture(){
    console.log("Uzunov");
    var new_picture = picture.cloneNode(true);
    document.body.appendChild(new_picture);
}
