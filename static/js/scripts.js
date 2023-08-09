var i = 0;
var imagesGallery1 = [
    "{% static 'images/colorfulDumplings0.jpg' %}",
    "{% static 'images/colorfulDumplings1.jpg' %}",
    "{% static 'images/colorfulDumplings2.PNG.jpg' %}",
];

var slideTime = 3000; // 3 seconds

function changePicture(imagesGalleryArray, galleryId) {
    var gallery = document.getElementById(galleryId);
    
    gallery.style.backgroundImage = "url(" + imagesGalleryArray[i] + ")";  // Use imagesGalleryArray
    
    if (i < imagesGalleryArray.length - 1) {  // Use imagesGalleryArray.length
        i++;
    } else {
        i = 0;
    }
    setTimeout(function () {
        changePicture(imagesGalleryArray, galleryId);  // Pass the arguments
    }, slideTime);
}

window.onload = function () {
    changePicture(imagesGallery1, 'gallery1');  // Pass the arguments
};