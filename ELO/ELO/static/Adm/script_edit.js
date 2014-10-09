$(document).ready(function(){

	// Caracteristicas do Dialog.
	$in_dialog = $(".inner_dialog").dialog({
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
	});

	$("#edit_form").on('submit', function(e){
		e.preventDefault();
		$dialog.dialog('close');

		data = $(this).serialize();
		data = data.slice(9, data.indexOf("&csrfmiddlewaretoken="));

		data = { username: data };

		$in_dialog.load("/assync/adm-info/", data, function(){
			$in_dialog.dialog('open');
		});
	});
});