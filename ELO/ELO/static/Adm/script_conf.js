$(document).ready(function(){

	$("#reg_form").on('submit', function(e){
		data = $(this).serialize();

		alert(data);
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
		    // hide the original submit button
		    $(this).find( "[type=submit]" ).hide();
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
