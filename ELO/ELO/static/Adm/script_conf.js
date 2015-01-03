$(document).ready(function(){

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
