$(document).ready(function () {
	$(".image").click(toggleImageView);
	$('.image').mouseenter(showOverlay);
	$('.image-overlay').mouseleave(hideOverlay);
	// $('.image').mouseout(hideOverlay)

})

const toggleImageView = e => {
	const imageId = e.target.id;
	$(`${imageId}`).toggleClass('showImage')
}

const showOverlay = e => {
	const imageId = e.target.previousElementSibling.id;
	$(`#${imageId}`).show('slow');
}

const hideOverlay = e => {
	$(`#${e.target.id}`).hide('slow')
}

const copyImageLink = e => {
	const inputWithUrl = e.parentNode.previousElementSibling;
	inputWithUrl.select();
	const c = navigator.clipboard.writeText(inputWithUrl.value)
}