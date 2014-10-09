$(document).ready(function(){
<<<<<<< HEAD

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

=======
>>>>>>> 198179b0ebd94d135f569e5a8565f286444d3203
	$("button[id^='edit_']").click(function(){
		field = $(this).attr("id").slice(5);
		fname = $(this).attr("title")

		// Gets the title of the dialog from the title of button.
<<<<<<< HEAD
		$(".dialog3").dialog("option", "title", fname);

		$(".dialog3").load("/assync/edit-field/"+field+"/");
		$(".dialog3").dialog("open");
=======
		$(".dialog").dialog("option", "title", fname);

		$(".dialog").load("/assync/edit-field/"+field+"/", function(){
			$(".dialog").dialog("open");
		});
>>>>>>> 198179b0ebd94d135f569e5a8565f286444d3203
	});
});