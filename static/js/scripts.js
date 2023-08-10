
var i = 0;
var imagesGallery1 = [
    '/static/images/colorfulDumplings0.jpg',
    '/static/images/colorfulDumplings1.jpg',
    '/static/images/colorfulDumplings6.jpg',
    '/static/images/colorfulDumplings2.PNG',
    '/static/images/colorfulDumplings3.PNG',
    '/static/images/colorfulDumplings4.jpeg',
    '/static/images/colorfulDumplings5.jpeg',
    '/static/images/colorfulDumplings7.jpg',
    '/static/images/colorfulDumplings8.jpg',
];

var slideTime = 3000; // 3 seconds
var fadeTime = 1000;  // 1 second (adjust as needed)

function changePicture(imagesGalleryArray, galleryId) {

    var gallery = document.getElementById(galleryId);
    
    gallery.style.opacity = '0'; // Start with opacity 0
    
    setTimeout(function () {
        gallery.style.backgroundImage = "url(" + imagesGalleryArray[i] + ")";
        gallery.style.opacity = '1'; // Fade in by setting opacity to 1
        if (i < imagesGalleryArray.length - 1) {
            i++;
        } else {
            i = 0;
        }
        setTimeout(function () {
            changePicture(imagesGalleryArray, galleryId);
        }, slideTime - fadeTime);
    }, fadeTime);
}

window.onload = function () {
    changePicture(imagesGallery1, 'gallery1');
};