// Array of image sources
const images = [
    'image1.jpg',
    'image2.jpg',
    'image3.jpg',
    'image4.jpg'
  ];
  
  // Initialize the current image index
  let currentImageIndex = 0;
  
  // Function to change the displayed image
  function changeImage(direction) {
    // Change the index based on direction
    if (direction === 'next') {
      currentImageIndex++;
      if (currentImageIndex >= images.length) {
        currentImageIndex = 0;  // Loop back to the first image
      }
    } else if (direction === 'previous') {
      currentImageIndex--;
      if (currentImageIndex < 0) {
        currentImageIndex = images.length - 1;  // Loop back to the last image
      }
    }
  
    // Update the image source based on the new index
    const galleryImage = document.getElementById('gallery-image');
    galleryImage.src = images[currentImageIndex];
  }
  