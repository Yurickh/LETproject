$(document).ready(function(){

	$(".dialog").dialog({
		autoOpen: false,
		hide: "slideUp",
		modal: true,
		resizable: false,
		});

	$("button[id^='edit_']").click(function(){
		field = $(this).attr("id").slice(5);
		fname = $(this).attr("title")

		// Gets the title of the dialog from the title of button.
		$(".dialog").dialog("option", "title", fname);

		$(".dialog").load("/assync/editfield/"+field);
		$(".dialog").dialog("open")
	});

	$("#interests_form").select2({
		allowClear: true,
		tokenSeparator: [",", " "],
		ajax: {
				url: "/assync/JSON_interests",
				dataType: "json",
				quietMillis: 500,
				data: function(term, page) {
					return {
						q: term,
						page_limit: 10,
						page: page
					};
				},
				results: function(data, page) {
					var more = (page*10) < data.total;

					return {results:data, more:more};
				}
				
			  }
	});

});