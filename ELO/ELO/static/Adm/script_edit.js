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
					 act: action
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
				 act: action
			   };

		$in_dialog.load("/assync/adm-course/"+action+"/"+model+"/", data,
						function(){ 
			$in_dialog.dialog('open');
		});

	});

	$("#reg_form").on('submit', function(e){
		e.preventDefault();
		$dialog.dialog('close');

		data = $(this).serialize();
		uname = data.slice(9, data.indexOf("&userMatric="));
		umatric = data.slice(data.indexOf("&userMatric=")+12, data.indexOf("&userCampus="));
		ucampus = data.slice(data.indexOf("&userCampus=")+12, data.indexOf("&userSex="));
		usex = data.slice(data.indexOf("&userSex=")+9, data.indexOf("&userEmail="));
		umail = data.slice(data.indexOf("&userEmail=")+11, data.indexOf("&userPassword="));
		// convert %40 to @, since serialize transformed @ to %40
		umail = decodeURIComponent(umail);
		upass = data.slice(data.indexOf("&userPassword=")+14, data.indexOf("&csrfmiddlewaretoken="));
		model = $("div[id^='model_']").attr("id").slice(6);
		crsf = data.slice(data.indexOf("&csrfmiddlewaretoken=")+21);
		

		data = { username: uname,
				 userMatric: umatric,
				 userCampus: ucampus,
				 userSex: usex,
				 userEmail: umail,
				 userPassword: upass,
				 model: model,
				 act: action,
				 csrfmiddlewaretoken: crsf
			   };

		$in_dialog.load("/assync/adm-info/", data, function(){ 
			$in_dialog.dialog('open');
		});
		
		
	});

});
