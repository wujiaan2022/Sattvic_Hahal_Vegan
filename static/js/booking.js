
function showBookingForm(table, date, time) {
    document.getElementById("booking-form-section").style.display = "block";
    document.getElementById("selected-date").value = date; // Set the selected date
    document.getElementById("selected-time").value = time; // Set the selected time
    document.getElementById("selected-table").value = table; // Set the selected table name
}

// function showBookingForm(table, date, time) {
//     // Set the values of the hidden input fields
//     document.getElementById("selected-table").value = table;
//     document.getElementById("selected-date").value = date;
//     document.getElementById("selected-time").value = time;

//     // Display the booking form
//     document.getElementById("booking-form-section").style.display = "block";
// }