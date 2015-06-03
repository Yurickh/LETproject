$(document).ready(function(){

    function loadExercise(arr)
    {
        $a = $("#ans");
        $a.load("assync/exercise",
            {
                'exercise_id': $serial[0].value,
                'csrfmiddlewaretoken': serial[2].value
            });
    }

    $("#exercise").submit(function(ev){
        ev.preventDefault();
        serial = $(this).serializeArray();

        if(serial[1].name == "options" || serial[1].name == "blank" || serial[1].name == "bloat")
            loadExercise(serial);
        
    });
});