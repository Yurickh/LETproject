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

	$("#Student").click(function(){
		$(".container").load("/adm/student");
	});

	//	Cria o evento de abertura dos formulários de registro, edição ou deleção
	/*		após clicar em qualquer button da home da Administração.
	$("button").click(function(){

		//	Coleta o título do button clicado na home de Adm.
		text_button = $(this).text();
		//	Transforma o título do button como título do dialog.
		$dialog.dialog("option", "title", text_button);

		//	Coleta a ação que irá ser realizada, sendo elas de
		//		registro, edição ou deleção.
		action = $(this).attr("id").slice(0,6);

		if (action == "insert"){
			//	Coleta o modelo sobre o qual a acao sera realizada, sendo eles
			//		estudante, professor ou curso.
			model = $(this).attr("id").slice(7);

			//	Faz uma requisicao AJAX passando a ação e o modelo adequado.
			//		Após a requisição enviada é passada a função de abertura do
			//		dialog.
			$dialog.load("/assync/adm-course/"+action+"/"+model+"/", function(){
				$dialog.dialog('open');
			});
		}
		else if (action == "srcdel"){

			model = $(this).attr("id").slice(7);

			$dialog.load("/assync/adm-edit/"+action+"/"+model+"/", function(){
				$dialog.dialog('open');
			});
			
		}
		else{
			action = $(this).attr("id").slice(0,3);

			model = $(this).attr("id").slice(4);

			$dialog.load("/assync/adm-course/"+action+"/"+model+"/", function(){
				$dialog.dialog('open');
			});
		}
	});
*/

});
