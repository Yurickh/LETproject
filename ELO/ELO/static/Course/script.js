$(document).ready(function(){

    $info = {'id': 0, 'slide':0};

    function loadLesson(less_id, slide)
    {
        $c = $('#container');
        $c.load("/assync/lesson/", 
            {'lesson_id':less_id, 
             'slide_number': slide,
             'csrfmiddlewaretoken': $.cookie('csrftoken')}, 
                function(){
                        $info.id = less_id;
                        $info.slide = slide;
            });
    }

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

		loadLesson(less_id, 0);
	});

    $("#l_bt_f").click(function(){
        loadLesson($info.id, $info.slide+1); 
    });

    $("#l_bt_b").click(function(){
        if($info.slide > 0)
            loadLesson($info.id, $info.slide-1);
    });
});
