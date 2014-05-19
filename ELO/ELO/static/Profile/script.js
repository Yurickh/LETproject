$(document).ready(function(){

	$(".dialog").dialog({
		autoOpen: false,
		hide: "slideUp",
		modal: true,
		resizable: false,
		show: "slideDown",
		});

	$("button[id^='edit_']").click(function(){
		field = $(this).attr("id").slice(5);
		$(".dialog").load("/assync/editfield/"+field);
		//$(".dialog").dialog("option", "position", {of: this})
		$(".dialog").dialog("open")
	});
});