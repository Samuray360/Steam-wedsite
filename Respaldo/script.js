function submitDonation() {
  const name = document.getElementById("name").value.trim();
  const lastName = document.getElementById("lastName").value.trim();
  const cardNumber = document.getElementById("cardNumber").value.trim();
  const cvv = document.getElementById("cvv").value.trim();
  const amount = document.getElementById("amount").value.trim();

  if (!name || !lastName || !cardNumber || !cvv || !amount) {
      alert("Please fill out all fields.");
      return;
  }

  if (!/^\d{16}$/.test(cardNumber)) {
      alert("Invalid Credit Card Number. It should be 16 digits.");
      return;
  }

  if (!/^\d{3,4}$/.test(cvv)) {
      alert("Invalid CVV. It should be 3 or 4 digits.");
      return;
  }

  if (isNaN(amount) || amount <= 0) {
      alert("Please enter a valid donation amount greater than 0.");
      return;
  }

  alert(`Thank you for your generous donation of $${amount}, ${name}!`);
}

