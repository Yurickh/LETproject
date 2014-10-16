$(document).ready(function(){
	$("#edit_form").on('submit', function(e){
		e.preventDefault();
		$dialog.dialog('close');

		data = $(this).serialize();
		uname = data.slice(9, data.indexOf("&csrfmiddlewaretoken="));
		crsf = data.slice(data.indexOf("&csrfmiddlewaretoken=")+21);
		model = $("div[id^='model_']").attr("id").slice(6);

		data = { username: uname,
				 csrfmiddlewaretoken: crsf,
				 model: model
			   };

		$in_dialog.load("/assync/adm-info/", data, function(){
			$in_dialog.dialog('open');
		});
	});
});
