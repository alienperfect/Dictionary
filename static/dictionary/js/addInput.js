function addInput(field){
	var div = document.getElementById(field);
    var button = document.getElementById('btn_' + field);

	if (div.style.display === 'none'){
		div.style.display = 'block';
        button.className = 'btn btn-primary';
	} else {
		div.style.display = 'none';
        button.className = 'btn btn-secondary';
	}
}