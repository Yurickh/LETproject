$(document).ready(function(){

	var index;
	var arr = $("#dlist").html().split(",");

	$("#interests_form #id_newdata").select2({
		tags: arr,
		tokenSeparators: [","]
	});

});