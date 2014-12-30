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

	$("#new_stu").click(function(){
		model = $("h2[id^='mod_']").attr("id").slice(4);
		$(".container").load("adm/new"+model+"/");
	});

	$("#reg_form").submit(function(e){
		e.preventDefault();

		var result = {}
		var postData = $(this).serializeArray();

		$.each( postData, function( i, pD ) {
  			result[pD.name] = pD.value;
      	});
	
      	model = $("h2[id^='mod_']").attr("id").slice(4);
      	result["model"] = model;
      	result["action"] = "reg";

		$load("adm/register",result);
	});
	
});
