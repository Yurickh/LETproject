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

	$("input[type^='submit']").click(function(){
		$(".dialog").dialog("close");
		alert('Usuário encontrado!');
		$(".dialog2").load("/assync/adm-info/");
		$(".dialog2").dialog("open");
=======

	$("#edit_form").on('submit', function(e){
		e.preventDefault();
		$dialog.dialog('close');

		data = $(this).serialize();
		uname = data.slice(9, data.indexOf("&csrfmiddlewaretoken="));
		crsf = data.slice(data.indexOf("&csrfmiddlewaretoken=")+21);

		data = { username: uname,
				 csrfmiddlewaretoken: crsf,
				 type: "info"
			   };

		$in_dialog.load("/assync/adm-info/", data, function(){
			$in_dialog.dialog('open');
		});
>>>>>>> 198179b0ebd94d135f569e5a8565f286444d3203
	});
});