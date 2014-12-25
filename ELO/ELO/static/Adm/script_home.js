$(document).ready(function(){

	//	Características do Dialog.
	$dialog = $(".dialog").dialog({
		autoOpen: false,
		show: {
			effect: "blind",
			duration: 1
		},
		hide: {
			effect: "blind",
			duration: 1
		},
		modal: true,
		resizable: false,

	});

	$in_dialog = $dialog;

	$in2_dialog = $dialog;

	$in3_dialog = $dialog;

	$("div[id^='mod_']").click(function(){
		model = $(this).attr("id").slice(4);

		$(".container").load("/adm/"+model);
	});

});
