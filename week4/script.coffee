$('.note').onmousedown = () ->
	this.mousemove = (e) ->
		this.posLeft = e.pageY and this.posTop = e.PageX
$('.note').onmouseup = () ->
	this.mousemove = null

make_note  = () ->
	$ '<textarea class="note">Text here</textarea>'
	
add_note = () -> 
	make_note().appendTo "section"

$(document).ready () ->
	$ 'button' .click = () ->
		add_note
 
