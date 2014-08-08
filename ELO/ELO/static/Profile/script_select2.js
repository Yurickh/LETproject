$(document).ready(function(){

	var index;
	var arr = $("#dlist").html().split(",");
	var farr;

	for(index=0; index < arr.length(); ++index)
		farr += {id: arr[index], text: arr[index]};

	$("#interests_form #id_newdata").select2({
		allowClear: true,
		tags: [],
		tokenSeparators: [",", " "],
		data: farr;
	});

});