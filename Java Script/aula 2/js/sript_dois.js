let lista = [
	"maça",
	"banana",
	"laranja",
	"uva",
	"pera",
	"abacaxi",
	"kiwi",
	"morango",
	"cereja",
	"melancia",
];

console.log(lista.length); // length exibe o tamanho da lista

let nome = "Jhonathan Souza Soares";
console.log("Quantidade de caracteres: " + nome.length); // length exibe o tamanho da string

if (nome.length > 25) {
	console.log("Nome grande.");
} else {
	console.log("Nome pequeno.");
}

// let nomeDois = prompt("Digite seu nome: ");

// console.log(lista[0]); // exibe o primeiro elemento da lista

// // colocando a lista de frutas no HTML
// for (let f = 0; f < lista.length; f++) {
// 	// console.log(lista[f]);
// 	document.getElementById("frutas").innerHTML += lista[f] + "<br>";
// }

// outra forma
let conteudo = "";
let div = document.getElementById("texto");
div.style.backgroundColor = "lightblue";

for (let f = 0; f < lista.length; f++) {
    conteudo += '<h2> '+lista[f] + "<br> </h2>";
}

div.innerHTML = conteudo; 

