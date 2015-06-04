$(document).ready(function(){

    function loadExercise(exercise)
    {

        $a = $("#ans");
        $a.load("/assync/exercise", exercise);

        
    }

    $("#exercise").submit(function(ev){
        ev.preventDefault();
        serial = $(this).serializeArray();

        exercise = {};

        for(i=0; i in serial; ++i)
            exercise[serial[i].name] = serial[i].value

        if("options" in exercise || "blank" in exercise || "bloat" in exercise)
            loadExercise(exercise);
        
    });
});