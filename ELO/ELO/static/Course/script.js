$(document).ready(function(){
    
    $accordion = $("#module_accordion").accordion({
        icons: {    "header": "ui-icon-plus",
                    "activeHeader": "ui-icon-minus"
                },
        heightStyle: 'fill'
    });

	
	$("div[class^='lesson_']").click(function(){
		less_id = $(this).attr("class").slice(7);

		$('#lesson_ctn').load("/assync/lesson/", {'lessonid':less_id});
	});
});
