$(document).ready(function(){

    // Lesson Listing

    $accordion = $("#module_accordion").accordion({
        icons: {    "header": "ui-icon-plus",
                    "activeHeader": "ui-icon-minus"
                },
        heightStyle: 'fill'
    });

    // Lesson Loading

	$("div[class^='lesson_']").click(function(){
		less_id = $(this).attr("class").slice(7);

		$('#lesson_ctn').load("/assync/lesson/", 
            {'lesson_id':less_id, 
             'csrfmiddlewaretoken': $.cookie('csrftoken')});
	});
});
