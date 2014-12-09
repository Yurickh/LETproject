$(document).ready(function(){

	$("#reg_form").on('submit', function(e){
		data = $(this).serialize();

		alert(data);

	});

	$("#reg2_form").on('submit', function(e){

		data2 = $(this).serialize();

		alert(data2);

		pass2 = data2.slice(12, data.indexOf("&csrfmiddlewaretoken="));

		alert(data);

		data.admPassword = pass2;

		alert(data.admPassword);
	});

	//data2 = { username: req.username,
	//		 userMatric: req.userMatric,
	//		 userCampus: req.userCampus,
	//		 userSex: req.userSex,
	//		 userEmail: req.userEmail,
	//		 userPassword: req.userPassword,
	//		 model: req.model,
	//		 act: req.act,
	//		 csrfmiddlewaretoken: req.csrfmiddlewaretoken
	//		};

	$in_dialog .dialog({
		open: function() {
		},
		buttons: [
			{
				text: "Confirm action",
				type: "submit",
				click: function() {
					$( this ).load("/assync/conf-adm/"+action+"/", data);		
					$( this ).dialog( "close" );
				},	
				form: "reg_form"
			},
			{
				text: "Cancel",
				click: function() {
					$( this ).dialog( "close" );
				}
			}
		]
	});

});
