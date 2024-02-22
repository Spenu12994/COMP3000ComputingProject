let lightLevel = 0;
let waterLevel = 0;
let pressureLevel = 0;

let lightGuagePort = 1;
let waterGuagePort = 2;
let pressureGuagePort = 3;
let pumpPort = 4;

var date = new Date;

const xValues = ["8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30"];
const yValues = [7,8,8,9,9,9,10,11,14,14,15];

const waterChart = new Chart(document.getElementById("waterChart"), {
    type: "line",
    data: {
      labels: xValues,
      datasets: [{
        fill: false,
        lineTension: 0,
        backgroundColor: "rgba(0,0,255,1.0)",
        borderColor: "rgba(0,0,255,0.1)",
        data: yValues
      }]
    },
    options: {
      legend: {display: false},
      scales: {
        yAxes: [{ticks: {min: 6, max:16}}],
      },
      title:{
        display: true,
        text: "Water Levels",
        fontSize: 16
      }
    }
});

const pressureChart = new Chart("pressureChart", {
    type: "line",
    data: {
      labels: xValues,
      datasets: [{
        fill: false,
        lineTension: 0,
        backgroundColor: "rgba(0,0,255,1.0)",
        borderColor: "rgba(0,0,255,0.1)",
        data: yValues
      }]
    },
    options: {
      legend: {display: false},
      scales: {
        yAxes: [{ticks: {min: 6, max:16}}],
      },
      title:{
        display: true,
        text: "Pressure Levels",
        fontSize: 16
      }
    }
});

const lightChart = new Chart("lightChart", {
    type: "line",
    data: {
      labels: xValues,
      datasets: [{
        fill: false,
        lineTension: 0,
        backgroundColor: "rgba(0,0,255,1.0)",
        borderColor: "rgba(0,0,255,0.1)",
        data: yValues
      }]
    },
    options: {
      legend: {display: false},
      scales: {
        yAxes: [{ticks: {min: 6, max:16}}],
      },
      title:{
        display: true,
        text: "Light Levels",
        fontSize: 16
      }
    }
});


// these functions were adapted from https://www.chartjs.org/docs/latest/developers/updates.html
function addData(chart, label, newData) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(newData);
    });
    chart.update();
}

function removeData(chart) {
    chart.data.labels.pop();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.pop();
    });
    chart.update();
}

 

 


function updateCharts(){
    

    var minutes = date.getSeconds();
    var hours = date.getHours();

    var currTimeText = hours.toString() + ":" + minutes.toString();

    addData(waterChart, currTimeText, Math.floor(Math.random() * 101));
    addData(pressureChart, currTimeText, Math.floor(Math.random() * 101));
    addData(lightChart, currTimeText, Math.floor(Math.random() * 101));

    removeData(waterChart);
    removeData(pressureChart);
    removeData(lightChart);
}

function water(){
    //enter code here to activate the watering system
    activate(pumpPort)
}

function activate(portNum){
    console.log("watering")
    //turn water valve on,
    //wait 3 seconds
    //turn water valve off
}

function updateWateringTimeframe(){
    //update the time difference between watering
}


function getGraphInfo(){
    //fetch the graph info from raspberry pi

    //lightLevel = lightGuagePort;
    //waterLevel = waterGuagePort;
    //pressureLevel = pressureGuagePort;

}

function updateGraphs(){
    //update the graph with get graph info
    //lightgraph.append = lightlevel
    //watergraph.append = waterlevel
    //pressurelevel.append = pressurelevel
}