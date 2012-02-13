<<<<<<< HEAD
make_note = () ->
	d = new Date()
	'<div class="note ui-draggable"><div class="title">'+d.getDate()+'/'+(d.getMonth()+1)+'/'+d.getFullYear()+' '+d.toTimeString().slice(0,5)+'</div><textarea></textarea></div>' 
=======
getActiveColor = () ->
	$(".active").attr("id")

make_note = () ->
	d = new Date()
	'<div class="note ui-draggable '+getActiveColor()+'"><div class="title">'+d.getDate()+'/'+(d.getMonth()+1)+'/'+d.getFullYear()+' '+d.toTimeString().slice(0,5)+'</div><textarea></textarea></div>' 

objectify_notes = () ->
	notes = new Array
	$('.note').each ->
		code_html = $(this).clone().wrap("div").parent().html().slice(9)
		value_html = $(this).children('textarea').val()
		notes[notes.length] = {code:code_html,text:value_html}
	localStorage.setItem("notes", JSON.stringify(notes))

append_note = (note) ->
	element = $(note['code'])
	$(element).children('textarea').val(note['text'])
	$("#pad").prepend(element)

deobjectify_notes = (notes) ->
	append_note(note) for note in notes

remove_note = (event, ui) ->
	ui.draggable.remove()
	objectify_notes()

>>>>>>> master
$(document).ready ->
	$("#make").click ->
		$("#pad").prepend(make_note()) 
		$(".note").draggable({ handle: "div.title", stack: ".note" })
<<<<<<< HEAD
	if typeof(localStorage) isnt 'undefined'
		notes = localStorage.getItem "notes"
		$("#pad").prepend(notes)
		$(".note").draggable({ handle: "div.title", stack: ".note" })
	$(document).keypress ->
		str = JSON.stringify $('.note')
		localStorage.setItem "notes" str
=======
	$(".colorpicker").click ->
		$(".active").removeClass("active")
		$(this).addClass("active")
	$("#remove").droppable({drop: remove_note})		
	if typeof(localStorage) isnt 'undefined'
		notes = JSON.parse(localStorage.getItem("notes"))
		if notes != null
			deobjectify_notes notes
			$(".note").draggable({ handle: "div.title", stack: ".note" })
	$(document).keyup ->
		objectify_notes()
		
>>>>>>> master
