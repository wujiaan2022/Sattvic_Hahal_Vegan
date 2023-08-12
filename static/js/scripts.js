
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

function createGallery(imagesGalleryArray, galleryId, textId) {
    var i = 0;
    var gallery = document.getElementById(galleryId);
    var text = document.getElementById(textId);
    var isHovered = false; // Track hover state

    var changePictureTimeout;
    var nextSlideTimeout;

    function showText() {
        text.style.opacity = '1';
    }
    
    function hideText() {
        text.style.opacity = '0';
    }
    
    function changePicture() {
        if (!isHovered) {
            gallery.style.opacity = '0';
            
            changePictureTimeout = setTimeout(function () {
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
    }

    function startSlide() {
        if (!isHovered) {
            changePicture();
        } else {
            showText();
        }
    }

    startSlide();

gallery.addEventListener('mouseenter', function () {
    isHovered = true;
    showText();
});
    
gallery.addEventListener('mouseleave', function () {
    isHovered = false;
    hideText();
    clearTimeout(changePictureTimeout);
    clearTimeout(nextSlideTimeout);
    startSlide();
});
}

window.onload = function () {
    createGallery(imagesGallery1, 'gallery1', 'gallery1-text');
    createGallery(imagesGallery3, 'gallery3', 'gallery3-text');
};