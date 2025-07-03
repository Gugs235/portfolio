console.log("oi, Iniciando o script");

async function getDados() {
	let dados_ibge = await fetch("https://servicodados.ibge.gov.br/api/v1/localidades/distritos");
    let cidades = document.querySelector(".cidades");
	let response = await dados_ibge.json();
    response = response.reverse(); // Inverte a ordem dos dados


    let conteudo = ''
    for (let i = 0; i < response.length ; i++) {
        conteudo += '<p> ID: ' + response[i].id + ' - Cidade: ' + response[i].nome + '</p> <br>';
    }

    cidades.innerHTML = conteudo;
}

getDados();
