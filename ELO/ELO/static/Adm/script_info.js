$(document).ready(function(){


	$("button[id^='del_']").click(function(e){
		e.preventDefault();
		$in_dialog.dialog('close');

		action = $(this).attr("id").slice(0,3);
		model = $(this).attr("id").slice(4);
		csrf = $("div[id^='csrf_']").attr("id").slice(5);
		uname = $("div[id^='username_']").attr("id").slice(9);

		if (model == "Course"){

			data = { courMatric: uname,
					 csrfmiddlewaretoken: crsf,
					 model: model,
					 act: action
					};
		}
		else{
			

			data = { username: uname,
					 csrfmiddlewaretoken: crsf,
					 model: model,
					 act: action
					};
		}

		$in2_dialog.load("/assync/adm-del/", data);
	});

	$("button[id^='edit_']").click(function(e){
		e.preventDefault();
		$in_dialog.dialog('close');

		model = $(this).attr("id").slice(5);
		field = $(this).attr("field");
		csrf = $("div[id^='csrf_']").attr("id").slice(5);
		uname = $("div[id^='username_']").attr("id").slice(9);

		data = { username: uname,
				 csrfmiddlewaretoken: crsf,
				 model: model,
				 act: action
				};

		$in2_dialog.load("assync/edit-field-adm/"+field+"/"+model+"/", data,
						function(){
			$in2_dialog.dialog('open');
		});

	});

});
