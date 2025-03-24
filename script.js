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


  function submitDonation() {
    const name = document.getElementById("name").value;
    const lastName = document.getElementById("lastName").value;
    const cvv = document.getElementById("cvv").value;
    const cardNumber = document.getElementById("cardNumber").value;

    if (!name || !lastName || !cvv || !cardNumber) {
        alert("Please fill out all fields.");
        return;
    }

    if (!/^[0-9]{3,4}$/.test(cvv)) {
        alert("Invalid CVV. It should be 3 or 4 digits.");
        return;
    }

    if (!/^[0-9]{16}$/.test(cardNumber)) {
        alert("Invalid Credit Card Number. It should be 16 digits.");
        return;
    }

    alert("Donation Successful! Thank you for your support.");
}

function scrollToForm() {
  document.getElementById("donationForm").scrollIntoView({ behavior: "smooth" });
}