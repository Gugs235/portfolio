let usuario = document.getElementById("usuario");

let span = document.getElementById("msg");

usuario.addEventListener("keyup", (event) => {
	console.log(event.target.value);

	span.textContent = event.target.value;
});

// let formulario = document.getElementById("calculator_form");
// let resultado = document.getElementById("resultado");

// formulario.igual.addEventListener("click", function (event) {
// 	event.preventDefault(); // Evita o envio do formulário

// 	num1 = parseFloat(formulario.num1.value);
// 	num2 = parseFloat(formulario.num2.value);

// 	console.log(num1);
// 	console.log(num2);

// 	let soma = num1 + num2;

// 	console.log("Soma: " + soma);
// });

let somar = document.getElementById("som");
let subtrair = document.getElementById("sub");
let divir = document.getElementById("divi");
let multiplicar = document.getElementById("mult");

somar.addEventListener("click", function (event) {
	event.preventDefault(); // Evita o envio do formulário
	let tela = document.getElementById("resultado");
	let num1 = parseFloat(document.getElementById("num1").value);
	let num2 = parseFloat(document.getElementById("num2").value);

	let soma = num1 + num2;

	tela.value = soma;
});

subtrair.addEventListener("click", function (event) {
	event.preventDefault(); // Evita o envio do formulário
	let tela = document.getElementById("resultado");
	let num1 = parseFloat(document.getElementById("num1").value);
	let num2 = parseFloat(document.getElementById("num2").value);

	let subtrai = num1 - num2;

	tela.value = subtrai;
});

divir.addEventListener("click", function (event) {
	event.preventDefault(); // Evita o envio do formulário
	let tela = document.getElementById("resultado");
	let num1 = parseFloat(document.getElementById("num1").value);
	let num2 = parseFloat(document.getElementById("num2").value);

	let divi = num1 / num2;

	tela.value = divi;
});

multiplicar.addEventListener("click", function (event) {
	event.preventDefault(); // Evita o envio do formulário
	let tela = document.getElementById("resultado");
	let num1 = parseFloat(document.getElementById("num1").value);
	let num2 = parseFloat(document.getElementById("num2").value);

	let multiplica = num1 * num2;

	tela.value = multiplica;
});
