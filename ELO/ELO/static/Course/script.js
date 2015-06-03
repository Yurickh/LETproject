$(document).ready(function(){

    $info = {'id': -1, 'slide':-1};

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

    // Lesson Listing2

    $accordion = $("#module_accordion").accordion({
        icons: {    "header": "ui-icon-plus",
                    "activeHeader": "ui-icon-minus"
                },
        heightStyle: 'fill'
    });

    $accordion.accordion("refresh");

    // Lesson Loading

	$("div[class^='lesson_']").click(function(){
		less_id = $(this).attr("class").slice(7);

		loadLesson(less_id, 0);
        $("#l_bt_f").removeAttr("disabled");
        $("#l_bt_b").attr("disabled", "disabled");
	});

    $("#l_bt_f").click(function(){
        if($info.id == -1) return;
        maxslides = $("div[class^='maxslides_']").attr("class").slice(10);
        if($info.slide < maxslides-2)
        {
            $("#l_bt_b").removeAttr("disabled");
            loadLesson($info.id, $info.slide+1);
        }
        else if($info.slide == maxslides-2)
        {
            loadLesson($info.id, $info.slide+1);
            $(this).attr('disabled', 'disabled');
        }
        else
            $(this).attr('disabled', 'disabled');
    });

    $("#l_bt_b").click(function(){
        if($info.slide > 1)
        {
            $("#l_bt_f").removeAttr("disabled");
            loadLesson($info.id, $info.slide-1);
        }
        else if($info.slide == 1)
        {
            loadLesson($info.id, 0);
            $(this).attr('disabled', 'disabled');
        }
        else
            $(this).attr('disabled', 'disabled');
    });


});

function dnd_alloWDrop(ev)
{
    ev.preventDefault();
}

function dnd_drag(ev)
{
    ev.dataTransfer.setData("text", ev.target.id)
}

function dnd_drop(ev)
{
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
}
