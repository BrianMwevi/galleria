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
	// $(`${e}`).tooltip('Text copied to clipboard');
	inputWithUrl.select();
	const c = navigator.clipboard.writeText(window.location.href + "static/"+ inputWithUrl.value)
}