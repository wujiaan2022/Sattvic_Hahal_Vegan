
var imagesGallery1 = [  
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014954/static/images/colorfulDumplings3.75404b5f2e0d.png',  
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014963/static/images/colorfulDumplings5.c9338c68bbc8.jpg',   
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014960/static/images/colorfulDumplings8.dfb0aacb97f1.jpg',  
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014947/static/images/colorfulDumplings4.858dea46089e.jpg',        
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014943/static/images/colorfulDumplings6.ae6285636c8f.jpg',
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014944/static/images/colorfulDumplings9.624029afa783.jpg',
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014938/static/images/colorfulDumplings2.ffbdb6332fef.png',    
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014939/static/images/colorfulDumplings7.7db791862e0a.jpg',  
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014957/static/images/colorfulDumplings1.312dd11c5cac.jpg', 
];

var imagesGallery3 = [
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014950/static/images/sattvicVegan8.b0e8214718c6.jpg',
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014951/static/images/sattvicVegan7.d571e8df8ec7.jpg',
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014953/static/images/sattvicVegan9.e7f5e547a890.jpg',
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014956/static/images/sattvicVegan3.004d20aa40df.jpg',
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014964/static/images/sattvicSetMenu2.5b41acfe8294.webp',
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014958/static/images/sattvicSetMenu8.ba624bf7d111.jpg',
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014946/static/images/sattvicVegan5.505e09208840.jpg',
    'https://res.cloudinary.com/drzvd9vpn/image/upload/v1694014941/static/images/sattvicVegan4.28b3626cb11b.jpg',   
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