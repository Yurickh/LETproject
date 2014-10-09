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

	$("input[type^='submit']").click(function(){
		$(".dialog").dialog("close");
		alert('Usuário encontrado!');
		$(".dialog2").load("/assync/adm-info/");
		$(".dialog2").dialog("open");
	});
});