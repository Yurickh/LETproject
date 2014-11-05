$(document).ready(function(){
	$("#edit_form").on('submit', function(e){
		e.preventDefault();
		$dialog.dialog('close');

		data = $(this).serialize();
		crsf = data.slice(data.indexOf("&csrfmiddlewaretoken=")+21);
		model = $("div[id^='model_']").attr("id").slice(6);

		if (model == "Course"){
			uname = data.slice(11, data.indexOf("&csrfmiddlewaretoken="));

			data = { courMatric: uname,
					 csrfmiddlewaretoken: crsf,
					 model: model,
					 action: action
					};
		}
		else{
			uname = data.slice(9, data.indexOf("&csrfmiddlewaretoken="));

			data = { username: uname,
					 csrfmiddlewaretoken: crsf,
					 model: model,
					 action: action
					};
		}

		$in_dialog.load("/assync/adm-info/", data, function(){
			$in_dialog.dialog('open');
		});
	});

	$("#insert_form").on('submit', function(e){
		e.preventDefault();
		$dialog.dialog('close');

		data = $(this).serialize();
		umatric = data.slice(11, data.indexOf("&csrfmiddlewaretoken="));
		crsf = data.slice(data.indexOf("&csrfmiddlewaretoken=")+21);
		model = $("div[id^='model_']").attr("id").slice(6);

		data = { courMatric: umatric,
				 csrfmiddlewaretoken: crsf,
				 model: model,
				 action: action
			   };

		$in_dialog.load("/assync/adm-course/"+action+"/"+model+"/", data,
						function(){ 
			$in_dialog.dialog('open');
		});

	});

	$("button").click(function(e){
		e.preventDefault();
		$in_dialog.dialog('close');

		username = data.username;
		action = $(this).attr("title").slice(3);
		model = $(this).attr("id").slice(4);

		data = { username: username,
				 action: action,
				 model: model
			   };

		$dialog.load("/assync/adm-edit/"+action+"/"+model+"/", data,
						function(){ 
			$dialog.dialog('open');
		});
	});	

});
