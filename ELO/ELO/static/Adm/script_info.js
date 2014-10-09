$(document).ready(function(){

	// Caracteristicas do Dialog.
	$(".dialog").dialog({
		autoOpen: false,
		show: {
			effect: "blind",
			duration: 1000
		},
		hide: {
			effect: "blind",
			duration: 1000
		},
		modal: true,
		resizable: false,
		stack: true,

	});

	$("button[id^='edit_']").click(function(){
		field = $(this).attr("id").slice(5);
		fname = $(this).attr("title")

		// Gets the title of the dialog from the title of button.
		$(".dialog3").dialog("option", "title", fname);

		$(".dialog3").load("/assync/edit-field/"+field+"/");
		$(".dialog3").dialog("open");
	});
});