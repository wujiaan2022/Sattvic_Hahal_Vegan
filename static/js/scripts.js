// List of image URLs
const gallery1_ImgChangeUrls = [
    colorfulDumplings0.jpg,
    colorfulDumplings1.jpg,
    colorfulDumplings2.PNG,
    colorfulDumplings3.PNG,
    colorfulDumplings4.jpeg,
    colorfulDumplings5.jpeg,
    colorfulDumplings6.jpg,
    colorfulDumplings7.jpg,
    colorfulDumplings8.jpg,
];

// Get a reference to the grid cell element
const gallery1_bg = document.getElementById('gallery1-imgChange');

// Function to change the background image
function gallery1_ImgChange() {
    const randomIndex = Math.floor(Math.random() * imageUrls.length);
    const randomImageUrl = imageUrls[randomIndex];
    gallery1-imgChange.style.backgroundImage = `url(${randomImageUrl})`;
}

// Call the function initially
gallery1_ImgChange();

// Automatically change the image every few seconds (e.g., every 5 seconds)
setInterval(changeBackgroundImage, 5000);