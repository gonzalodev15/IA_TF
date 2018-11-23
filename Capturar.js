$(document).ready(()=>{
    $('#Enviar').click(async ()=>{
    	var lis = [...document.getElementById("div2").getElementsByTagName("li")];
   		var Dinero = document.getElementById("Dinero");
   		var Procesador = document.getElementById("Procesador");
   		var Tarjeta = document.getElementById("Tarjeta");
   		var Ram = document.getElementById("Ram");

    	var auxDinero = Dinero.options[Dinero.selectedIndex].value;
    	var auxProcesador = Procesador.options[Procesador.selectedIndex].value;
    	var auxTarjeta = Tarjeta.options[Tarjeta.selectedIndex].value;
    	var auxRam = Ram.options[Ram.selectedIndex].value;
		
		let data = {
			lista_juegos: lis.map((ele, i) => ele.value),
			dinero: auxDinero,
			procesador: auxProcesador,
			tarjeta_video: auxTarjeta,
			ram: auxRam
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

		//console.log(await res.json());
		document.getElementById("respuestas").innerHTML = await printResponses(await res.json())
    });
});

async function printResponses(obj) {
	let array = obj.respuesta;
	let component = "<ul class='list-group'>";
	array.forEach((element, index) => {
		component += `<li class="list-group-item">Opcion ${index}: ${element}</li>`;
	});
	component += "</ul>";
	return component;
}