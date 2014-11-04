$(document).ready(function(){
	
	$("#refresh").click(function(){
		$dialog.load("/assync/adm-course/"+action+"/"+model+"/", data,
			function(){ $dialog.dialog('open');
		});
	});	
});
