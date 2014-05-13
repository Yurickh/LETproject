$(document).ready(function(){

	$("div[class^='edit_']").click(function(){
		field = $(this).attr("class").slice(5);
		$("div[class^='editform_']").toggle();
		$(".editform_"+field).load("/assync/editfield/"+field);
		$(".editform_"+field).toggle();
	});
});