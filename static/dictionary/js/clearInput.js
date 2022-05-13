function clearInput(){
	var buttons = document.getElementById('buttons').children;

	for (let i = 0; i < buttons.length; i++){
		let button = buttons[i];
		if (button.className === 'btn btn-secondary'){
			field = button.id.slice(4);
			let input = document.getElementById('id_' + field);
			input.value = '';
		}
	}
}