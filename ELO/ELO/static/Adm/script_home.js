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


	// Cria o evento de clicar e abrir os buttons da pagina de adm.
	$("button").click(function(){
		// Coleta o modelo sobre o qual a acao sera realizada, sendo eles
		// estudante, professor ou curso.
		model = $(this).attr("id").slice(4);
		// Coleta a acao que ira ser realizada, sendo elas de
		// registro, edicao ou delecao.
		text_button = $(this).text();
		action = text_button.substr(0, text_button.indexOf(' ')).toLowerCase()

		// Transforma o titulo do button como titulo do dialog.
		$(".dialog").dialog("option", "title", text_button);

		// Faz uma requisicao AJAX passando a acao e o modelo adequado.
		$(".dialog").load("/assync/adm-edit/" + action + "/" + model + "/");

		// Abre o dialog
		$(".dialog").dialog("open");
		
	});

});
