function count() {
	document.getElementById('status').innerHTML = "requesting...";
	var request = new XMLHttpRequest();
	request.open('GET','http://50apps-week3.appspot.com/results.json',false);
	request.send(document.getElementById('url').value);
	if (request.status === 0) {
		document.getElementById('results').innerHTML = request.responseText;
		document.getElementById('status').innerHTML = "";
	}
	else {
		docuemnt.getElementById('status').innerHTML = "failed";
	}
}
