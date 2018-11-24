$(document).ready(()=>{
    $('#Enviar').click(async ()=>{
    	var lis = [...document.getElementById("div2").getElementsByTagName("li")];
   		
		console.log(lis.map((ele, i) => ele.id));
		let data = {
			sintomas: lis.map((ele, i) => ele.id)
		};

		console.log(data);

		let res = await fetch('http://localhost:5000/logic', {
			method: 'POST',
			body: JSON.stringify(data),
			headers: {
				"Origin": "http://localhost:5000",
				"Access-Control-Request-Method": "POST",
				"Access-Control-Request-Headers": "Content-Type"
			}
		});

		result = await res.json();
		document.getElementById("respuestas").innerHTML = printResponses(result);
    });
});

function printResponses(obj) {
	let array = obj.respuesta;
	let component = "<ul class='list-group'>";
	array.forEach((element, index) => {
		component += `<li class="list-group-item">${element}</li>`;
	});
	component += "</ul>";
	return component;
}