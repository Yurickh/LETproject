$(document).ready(function(){

	$(".dialog").dialog({
		autoOpen: false,
		hide: "slideUp",
		modal: true,
		resizable: false,
		show: "slideDown",
		});

	$("div[class^='edit_']").click(function(){
		field = $(this).attr("class").slice(5);
		$(".dialog").load("/assync/editfield/"+field);
		//$(".dialog").dialog("option", "position", {of: this})
		$(".dialog").dialog("open")
	});
});