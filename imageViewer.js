const modal = document.getElementById("image-modal");
	const modalImage = document.getElementById("modal-image");
	const closeBtn = document.getElementsByClassName("close")[0];
	const images = document.querySelectorAll(".grid-image");

	images.forEach(image => {
		image.addEventListener("click", () => {
			modal.style.display = "flex";
			modalImage.src = image.src;
		});
	});

	closeBtn.addEventListener("click", () => {
		modal.style.display = "none";
	});

	modal.addEventListener("click", (e) => {
		if (e.target === modal) {
			modal.style.display = "none";
		}
	});