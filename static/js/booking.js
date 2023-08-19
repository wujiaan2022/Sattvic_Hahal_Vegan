function showTableAvailability() {
    // Hide the initial form section
    // document.getElementById("initial-form-section").style.display = "none";
    
    // Show the table availability section
    document.getElementById("table-availability-section").style.display = "block";
}

function showBookingForm(tableNumber) {
    // Hide the table availability section
    document.getElementById("table-availability-section").style.display = "none";
    
    // Show the booking form section for the selected table
    document.getElementById("booking-form-section").style.display = "block";
    
    // Update the hidden field's value to the selected table number
    document.getElementById("selected-table-number").value = tableNumber;
}