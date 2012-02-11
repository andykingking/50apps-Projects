make_note = () ->
	d = new Date()
	'<div class="note ui-draggable"><div class="title">'+d.getDate()+'/'+(d.getMonth()+1)+'/'+d.getFullYear()+' '+d.toTimeString().slice(0,5)+'</div><textarea></textarea></div>' 
$(document).ready ->
	$("#make").click ->
		$("#pad").prepend(make_note()) 
		$(".note").draggable({ handle: "div.title", stack: ".note" })
	if typeof(localStorage) isnt 'undefined'
		notes = localStorage.getItem "notes"
		$("#pad").prepend(notes)
		$(".note").draggable({ handle: "div.title", stack: ".note" })
	$(document).keypress ->
		str = JSON.stringify $('.note')
		localStorage.setItem "notes" str
