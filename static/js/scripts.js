
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
    '/static/images/colorfulDumplings9.jpg'
];

var imagesGallery3 = [
    '/static/images/sattvicVegan2.jpeg',
    '/static/images/sattvicVegan3.jpg',
    '/static/images/sattvicVegan4.jpeg',
    '/static/images/sattvicVegan5.jpg',
    '/static/images/sattvicVegan6.jpeg',
    '/static/images/sattvicVegan7.jpeg',
    '/static/images/sattvicVegan8.jpg',
    '/static/images/sattvicVegan9.jpeg',   
];

var slideTime = 3000;
var fadeTime = 1000;


function changePicture(imagesGalleryArray, galleryId) {
   
    var gallery = document.getElementById(galleryId);
    
    gallery.style.opacity = '0'; // Start with opacity 0      

    var timer = setTimeout(function () {
         
        gallery.style.backgroundImage = "url(" + imagesGalleryArray[i] + ")";
        gallery.style.opacity = '1'; // Fade in by setting opacity to 1
        if (i < imagesGalleryArray.length - 1) {
            i++;
        } else {
            i = 0;
        }
        
       setTimeout(function () {
            changePicture(imagesGalleryArray, galleryId);
        }, slideTime-fadeTime);        
        

    }, fadeTime); 

    gallery.addEventListener("mouseenter", function() {
        timer.pause()
    });
    
    gallery.addEventListener("mouseleave", function() {
        timer.play()
    });

}   
    

window.onload = function () {
    changePicture(imagesGallery1, 'gallery1');
    changePicture(imagesGallery3, 'gallery3');
};


