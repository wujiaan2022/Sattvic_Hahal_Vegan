
var imagesGallery1 = [  
    '/static/images/colorfulDumplings9.jpg',  
    '/static/images/colorfulDumplings8.jpg',   
    '/static/images/colorfulDumplings5.jpeg',  
    '/static/images/colorfulDumplings7.jpg',        
    '/static/images/colorfulDumplings2.PNG',
    '/static/images/colorfulDumplings3.PNG',
    '/static/images/colorfulDumplings4.jpeg',    
    '/static/images/colorfulDumplings6.jpg',  
    '/static/images/colorfulDumplings1.jpg', 
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

function createGallery(imagesGalleryArray, galleryId) {
    var i = 0;
    var gallery = document.getElementById(galleryId);
        
    var showPictureTimeout;
    var nextSlideTimeout;

          
    function changePicture() {
        
        gallery.style.opacity = '0';
        
        showPictureTimeout = setTimeout(function () {
            gallery.style.backgroundImage = "url(" + imagesGalleryArray[i] + ")";
            gallery.style.opacity = '1';
            
            if (i < imagesGalleryArray.length - 1) {
                i++;
            } else {
                i = 0;
            }
            
            nextSlideTimeout = setTimeout(function () {
                changePicture();
            }, slideTime - fadeTime);

        }, fadeTime);
        
    }

    changePicture();

gallery.addEventListener('mouseenter', function () {
    
    clearTimeout(showPictureTimeout);
    clearTimeout(nextSlideTimeout);
});
    
gallery.addEventListener('mouseleave', function () {
            
    changePicture();
});
}

window.onload = function () {
    createGallery(imagesGallery1, 'gallery1');
    createGallery(imagesGallery3, 'gallery3');
};