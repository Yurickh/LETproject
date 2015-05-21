$(document).ready(function(){

	//	Características do Dialog.
	$dialog = {
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
	};

	$in_dialog = $dialog;

	$in2_dialog = $dialog;

	$in3_dialog = $dialog;

	//	Cria o evento de abertura dos formulários de registro, edição ou deleção
	//		após clicar em qualquer button da home da Administração.
	$("button").click(function(){

		//	Coleta o título do button clicado na home de Adm.
		text_button = $(this).text();
		//	Transforma o título do button como título do dialog.
		$dialog.dialog("option", "title", text_button);

		//	Coleta a ação que irá ser realizada, sendo elas de
		//		registro, edição ou deleção.
		action = $(this).attr("id").slice(0,6);

	$("div[id^='mod_']").click(function(){
		model = $(this).attr("id").slice(4);

		$(".container").load("/adm/src"+model+"/");
	});
});
