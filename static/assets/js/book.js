
/**

* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated booking's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific booking.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

document.addEventListener("DOMContentLoaded", function() {
  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");


  for (let button of deleteButtons) {
      button.addEventListener("click", (e) => {
          let bookingId = e.target.getAttribute("data-booking_id");
          deleteConfirm.href = `/bookingstablestays/delete_booking/${bookingId}/`;  // Correct the URL pattern
          deleteModal.show();
      });
  }
});

