document.addEventListener("DOMContentLoaded", function() {
  const editReviewModal = new bootstrap.Modal(document.getElementById("editReviewModal"));
  const modalReviewForm = document.getElementById("modalReviewForm");
  const modalSubmitButton = document.getElementById("modalSubmitButton");
  const reviewText = document.getElementById("id_comment"); // Assuming this is the ID of your comment field

  const editButtons = document.getElementsByClassName("btn-edit");
  for (let editbutton of editButtons) {
      editbutton.addEventListener("click", (e) => {
          let reviewId = e.target.getAttribute("data-review_id");
          let reviewContent = document.getElementByClass(`review${reviewId}`).innerText.trim();
          reviewText.value = reviewContent; // Populate the textarea with existing review content
          modalReviewForm.setAttribute("action", `/review_edit/${reviewId}/`); // Set the form action dynamically
          modalSubmitButton.innerText = "Update"; // Change submit button text
          editReviewModal.show(); // Show the modal
      });
  }

  if (modalSubmitButton) {
      modalSubmitButton.addEventListener("click", () => {
          modalReviewForm.submit(); // Submit the form when Save changes is clicked
      });
  }
});
