// function showTableAvailability() {
//     // Hide the initial form section
//     // document.getElementById("initial-form-section").style.display = "none";
    
//     // Show the table availability section
//     document.getElementById("table-availability-section").style.display = "block";
// }

// function showBookingForm(table) {
//     // Display the booking form section
//     document.getElementById("booking-form-section").style.display = "block";
    
//     // Set the value of the selected_table input
//     document.getElementById("selected-table").value = table.table_name;
//   }


function showBookingForm(table, date, time) {
    document.getElementById("booking-form-section").style.display = "block";
    document.getElementById("selected-table-number").value = table;
    document.getElementById("booking-date").value = date; // Set the date in the form
    document.getElementById("booking-time").value = time; // Set the time in the form
}