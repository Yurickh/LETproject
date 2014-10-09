$(document).ready(function(){


	$("button[id^='edit_']").click(function(){
		field = $(this).attr("id").slice(5);
		fname = $(this).attr("title")

		// Gets the title of the dialog from the title of button.
		$(".dialog").dialog("option", "title", fname);

		$(".dialog").load("/assync/edit-field/"+field+"/", function(){
			$(".dialog").dialog("open");
		});
	});
});