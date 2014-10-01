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
	});

	// Cria o evento de clicar e abrir os buttons da pagina de adm.
	$(".but").click(function(){
		// Coleta a acao que ira ser realizada, sendo elas de
		// registro, edicao ou delecao.
		text_button = $(this).text();

		// Transforma o titulo do button como titulo do dialog.
		$(".dialog").dialog("option", "title", text_button);

		// Abre o dialog
		$(".dialog").dialog("open");
		// Faz uma requisicao AJAX passando a acao e o modelo adequado.
		$(".dialog").load("/assync/adm-info/");
		
	});

});
