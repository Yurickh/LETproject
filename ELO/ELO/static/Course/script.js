$(document).ready(function(){
    
    $accordion = $("#module_accordion").accordion({
        collapsible: true,
        active: false,
        icons: {    "header": "ui-icon-plus",
                    "activeHeader": "ui-icon-minus"
                },
        heightStyle: 'content'
    });
});
