function graph_data(obj) {
	var myChart = new JSChart('results', 'bar');
	myChart.setDataArray(obj['top10']);
	myChart.setTitle("Top 10 words by frequency");
	myChart.setAxisNameX('Word');
	myChart.setAxisPaddingLeft(80);
	myChart.setAxisNameY('Frequency');
	myChart.setAxisPaddingBottom(50);
	myChart.setAxisReversed(true);
	myChart.draw();
	document.getElementById('longest').innerHTML = "Longest word: " + obj['longest'];
	document.getElementById('shortest').innerHTML = "Shortest word: " + obj['shortest'];
}

function count() {
	document.getElementById('status').innerHTML = "requesting...";
	var request = new XMLHttpRequest();
	request.open('POST','/results.json',true);
	request.onreadystatechange = function (e) {
		if (request.readyState === 4) {
			if (request.status === 200) {
				graph_data(JSON.parse(request.responseText));
				document.getElementById('status').innerHTML = "";
			}
			else {
				document.getElementById('status').innerHTML = "failed";
			}
		}
	}
	request.send(document.getElementById('url').value);
}
