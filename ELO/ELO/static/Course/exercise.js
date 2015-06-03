function loadExercise(arr)
{
    $a = $("#ans");
    $a.load("assync/exercise",
        {
            'lesson_id': $info.id,
            'slide_number': $info.slide,
            'csrfmiddlewaretoken': serial[1].value
        });
}

$("#exercise").submit(function(ev){
    ev.preventDefault();
    serial = $(this).serializeArray();


    // Se a pergunta foi respondida
    if(serial[0].name == "options" || serial[0].name == "blank" || serial[0].name == "bloat")
        loadExercise(serial);
    
});