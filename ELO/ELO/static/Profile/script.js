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

	//stylizes the interests text
	/*$("#interests").on("input", function(){
		$inter = $("#interests");
		str = $.trim($inter.text());
		if(str.slice(-1) == ',')
		{
			str = str.split(',');
			strfin = "";

			for (i in str)
				if(str[i].slice(0, 26) != '<div class="interest_node">'
					strfin += '<div class="interest_node">' + str[i] + '</div>';
				else
					strfin += str[i];

			html = $.parseHTML( strfin );
			$inter.empty();
			$inter.append(html);
		}
	});*/
});