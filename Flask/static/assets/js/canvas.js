
function renderGraph(cotacao, horario) {
  let graph = new Chart(document.querySelector("#line-chart"), {
    type: 'line',
    data: {
      labels: horario, // Datas - Vetor 
      datasets: [{
        data: cotacao, // Dados - Vetor Datas.length == Dados.length"
        label: "Valor Bit Coin",
        borderColor: "#3e95cd",
        fill: false,
        scaleLabel: '$'
      },
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Valor Diario e por mes '
      }
    }
  });
}


// Cabecalho da requisicao
var txt = '';
let cotacao = [];
let horario = [];

var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function(){
  if(xmlhttp.status == 200 && xmlhttp.readyState == 4){
    let dadosBrutos = JSON.parse(xmlhttp.responseText);

    for (let item of dadosBrutos['documents']) {
      cotacao.push(item["preço"]);
    };

  }
};

xmlhttp.open("GET","./getCotacao",true);
xmlhttp.send();

var xmlhttp2 = new XMLHttpRequest();
xmlhttp2.onreadystatechange = function(){
  if(xmlhttp2.status == 200 && xmlhttp2.readyState == 4){
    let dadosBrutos = JSON.parse(xmlhttp2.responseText);
    for (let item of dadosBrutos['documents']) {
      horario.push(item["horario"].replace("/", ":").substring(0, 5));

    };

    renderGraph(cotacao, horario);

  }
};

xmlhttp2.open("GET","./getHoras",true);
xmlhttp2.send();


let datas;

