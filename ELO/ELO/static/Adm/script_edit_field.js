$(document).ready(function(){
	$("form[id^='_form']").on('submit', function(e){
		e.preventDefault();
		$in2_dialog.dialog('close');

		alert(ff);
	};


});