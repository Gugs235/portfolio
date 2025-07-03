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
	conteudo += "<h2> " + lista[f] + "<br> </h2>";
}

div.innerHTML = conteudo;

let dicionario = {
	nome: "Jhonathan",
	idade: 25,
	altura: 1.8,
	profissao: "Programador",
	linguagens: ["JavaScript", "Python", "Java"],
};

let texto = document.getElementById("texto");
texto.innerHTML =
	dicionario.nome +
	"<br>" +
	dicionario.idade +
	"<br>" +
	dicionario.altura +
	"<br>" +
	dicionario.profissao +
	"<br>" +
	dicionario.linguagens.join(", ");

// console.log(dicionario.nome); // exibe a idade
// console.log(dicionario.idade); // exibe a idade
// console.log(dicionario.altura); // exibe a idade
// console.log(dicionario.profissao); // exibe a idade
// console.log(dicionario.linguagens); // exibe a idade

let lista_pessoas = [
	{
		"nome": "Jonas",
		"idade": 25,
		"altura": 1.8,
		"profissao": "Programador",
	},
	{
		"nome": "Maria",
		"idade": 30,
		"altura": 1.65,
		"profissao": "Designer",
	},
	{
		"nome": "Pedro",
		"idade": 28,
		"altura": 1.75,
		"profissao": "ADS",
	},
	{
		"nome": "Josefa",
		"idade": 22,
		"altura": 1.7,
		"profissao": "Programadora",
	},
	{
		"nome": "João",
		"idade": 35,
		"altura": 1.85,
		"profissao": "Engenheiro",
	},
];

// console.log(lista_pessoas[2]);

console.log(lista_pessoas[2].nome) +
	lista_pessoas[2].idade +
	lista_pessoas[2].altura +
	lista_pessoas[2].profissao;

// console.log(lista_pessoas[2].nome + " tem " + lista_pessoas[2].idade + " anos."); // exibe o nome e a idade da primeira pessoa

for (let i = 0; i < lista_pessoas.length; i++) {
	conteudo +=
		"<p> Nome: " +
		lista_pessoas[i].nome +
		"<br>" +
		"Idade: " +
		lista_pessoas[i].idade +
		"<br>" +
		"Altura: " +
		lista_pessoas[i].altura +
		"<br>" +
		"Profissão: " +
		lista_pessoas[i].profissao +
		"</p>";
}
texto.innerHTML = conteudo;
