$(document).ready(function(){

    $dialog = $(".dialog").dialog({
        autoOpen: false,
        hide: "slideUp",
        modal: true,
        resizable: false,
        });

    $("button[id^='edit_']").click(function(){
        field = $(this).attr("id").slice(5);
        fname = $(this).attr("title")

        // Gets the title of the dialog from the title of button.
        $dialog.dialog("option", "title", fname);

        $dialog.load("/assync/editfield/"+field, function(){
            $dialog.dialog("open");
        });
    });

});