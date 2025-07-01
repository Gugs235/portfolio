// alert("Olá Mundo!!");
// alert("Bem vindo ao meu site!");

console.log("Mensaaagem no console"); //é cimilar ao print do python

var btn_cor = document.getElementById("btn_color");
var btn_cor2 = document.getElementById("btn_color2");
var btn_mais = document.getElementById("btn_plus");
var btn_menos = document.getElementById("btn_less");
var btn_click = document.getElementById("btn_click");

var contador = parseInt(document.querySelector("#texto").textContent);
//textContent é usado para pegar o texto de um elemento

console.log(contador);
console.log(typeof contador);

btn_mais.addEventListener("click", function () {
	contador++;

	document.querySelector("#texto").textContent = contador; // Atualiza o texto do elemento com o novo valor
});

btn_menos.addEventListener("click", function () {
	contador--;

	document.querySelector("#texto").textContent = contador; // Atualiza o texto do elemento com o novo valor
});

var header = document.querySelector(".cabecalho");

header.addEventListener("mouseover", function () {
	header.style.backgroundColor = "brown";
	header.style.color = "lightgreen";
});

header.addEventListener("mouseout", function () {
	header.style.backgroundColor = "lightgreen";
	header.style.color = "brown";
});

function mudacor() {
	// alert("Mudando a cor do texto");
	// var div2 = document.getElementsByClassName("div_texto");
	var div = document.querySelector(".div_texto");
	var container = document.getElementById("container_btns");

	div.style.backgroundColor = "red";
	container.style.backgroundColor = "blue";
}

function mudacor2() {
	// alert("Mudando a cor do texto");
	// var div2 = document.getElementsByClassName("div_texto");
	var div = document.querySelector(".div_texto");
	var container = document.getElementById("container_btns");

	container.style.backgroundColor = "aqua";
	div.style.backgroundColor = "yellow";
}

function postar() {
	alert("Clicoooouu");
}

btn_cor.addEventListener("click", mudacor);
btn_cor2.addEventListener("click", mudacor2);
btn_click.addEventListener("click", postar);
