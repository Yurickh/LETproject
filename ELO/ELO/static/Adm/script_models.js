$(document).ready(function(){

	$("#acc_search").submit(function(e){
		e.preventDefault();

		var result = {}
		var postData = $(this).serializeArray();

		$.each( postData, function( i, pD ) {
      			result[pD.name] = pD.value;
	      	});
	
	      	model = $("h2[id^='mod_']").attr("id").slice(4);
	      	result["model"] = model;

		$(".container").load("adm/"+model+"/", result);
	});
	
});
