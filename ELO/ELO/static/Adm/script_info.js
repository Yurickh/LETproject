$(document).ready(function(){


	$("button[id^='del_']").click(function(e){
		e.preventDefault();
		$in_dialog.dialog('close');

		action = $(this).attr("id").slice(0,3);
		model = $(this).attr("id").slice(4);
		csrf = $("div[id^='csrf_']").attr("id").slice(5);

		if (model == "Course"){
			uname = $("div[id^='username_']").attr("id").slice(9);

			data = { courMatric: uname,
					 csrfmiddlewaretoken: crsf,
					 model: model,
					 action: action
					};
		}
		else{
			uname = $("div[id^='username_']").attr("id").slice(9);

			data = { username: uname,
					 csrfmiddlewaretoken: crsf,
					 model: model,
					 action: action
					};
		}

		$in2_dialog.load("/assync/adm-del/", data);
	});

	$("button[id^='edit_']").click(function(e){
		e.preventDefault();
		$in_dialog.dialog('close');

		model = $(this).attr("id").slice(5);
		field = $(this).attr("field");

		$in2_dialog.load("assync/edit-field-adm/"+field+"/"+model+"/", function(){
			$in2_dialog.dialog('open');
		});

	});

});
