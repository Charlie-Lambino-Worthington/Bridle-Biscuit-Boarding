document.addEventListener("DOMContentLoaded", function() {
  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");

const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_body");
const modalReviewForm = document.getElementById("modalReviewForm");
const modalSubmitButton = document.getElementById("modalSubmitButton");
const editReviewModal = new bootstrap.Modal(document.getElementById("editReviewModal"));

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific review.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
  for (let button of deleteButtons) {
      button.addEventListener("click", (e) => {
          let reviewId = e.target.getAttribute("data-review_id");
          deleteConfirm.href = `/bookingstablestays/delete_review/${reviewId}/`;  // Correct the URL pattern
          deleteModal.show();
      });
  }
});
/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Fetches the content of the corresponding review.
* - Populates the `reviewText` input/textarea with the review's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_review/{reviewId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    let reviewContent = document.getElementById(`review${reviewId}`).innerText.trim();
    reviewText.value = reviewContent;
    modalReviewForm.setAttribute("action", `/edit_review/${reviewId}/`);
    modalSubmitButton.innerText = "Update";
    editReviewModal.show();
  });
}

modalSubmitButton.addEventListener("click", () => {
  modalReviewForm.submit();
});


