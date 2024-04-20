let lightLevel = 0;
let waterLevel = 0;
let tempLevel = 0;

let lightGuagePort = 1;
let waterGuagePort = 2;
let tempGuagePort = 3;
let pumpPort = 4;



const xValues = ["8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30"];
const yValues = [7,8,8,9,9,9,10,11,14,14,15];
const waterValues = [7,8,8,9,9,9,10,11,14,14,15];
const tempValues = [23,24,22,20,24,25,19,21,23,22,24];
const lightValues = [7,8,8,9,9,9,10,11,14,14,15];

const waterChart = new Chart(document.getElementById("waterChart"), {
    type: "line",
    data: {
      labels: xValues,
      datasets: [{
        fill: false,
        lineTension: 0,
        backgroundColor: "rgba(0,0,255,1.0)",
        borderColor: "rgba(0,0,255,0.1)",
        data: waterValues
      }]
    },
    options: {
      legend: {display: false},
      scales: {
        yAxes: [{ticks: {min: 0, max:16}}],
      },
      title:{
        display: true,
        text: "Water Levels",
        fontSize: 16
      }
    }
});

const tempChart = new Chart("tempChart", {
    type: "line",
    data: {
      labels: xValues,
      datasets: [{
        fill: false,
        lineTension: 0,
        backgroundColor: "rgba(0,0,255,1.0)",
        borderColor: "rgba(0,0,255,0.1)",
        data: tempValues
      }]
    },
    options: {
      legend: {display: false},
      scales: {
        yAxes: [{ticks: {min: 0, max:50}}],
      },
      title:{
        display: true,
        text: "Temperature Levels",
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
        data: lightValues
      }]
    },
    options: {
      legend: {display: false},
      scales: {
        yAxes: [{ticks: {min: 0, max:16}}],
      },
      title:{
        display: true,
        text: "Light Levels",
        fontSize: 16
      }
    }
});


// these functions were adapted from https://www.chartjs.org/docs/latest/developers/updates.html
function addData(chart, chartTxt, newData) {
    
    switch(chartTxt){
        case "waterChart":
            waterValues.push(newData);
            break;
        case "tempChart":
            tempValues.push(newData);
            break;
        case "lightChart":
            lightValues.push(newData);
            break;
        default:
            yValues.push(newData);
    }
    
    chart.update();
}

function removeData(chart, chartTxt) {
    switch(chartTxt){
        case "waterChart":
            waterValues.shift();
            break;
        case "tempChart":
            tempValues.shift();
            break;
        case "lightChart":
            lightValues.shift();
            break;
        default:
            yValues.shift();
    }
    
    chart.update();
}

 

 


function updateCharts(){// this should update with our data reading hardware every alloted time frame (such as every 30 minutes)
    var date = new Date;
    var minutes = date.getMinutes();
    var hours = date.getHours();

    var currTimeText = hours.toString() + ":" + minutes.toString();

    xValues.push(currTimeText);
    xValues.shift();

    addData(waterChart, "waterChart",Math.floor(Math.random() * 16)); //math.random is used to simulate a response from our hardware, once implemented our data values from hardware will be inputted here instead
    addData(tempChart, "tempChart", Math.floor(Math.random() * 16));
    addData(lightChart,"lightChart",Math.floor(Math.random() * 16));

    
    removeData(waterChart, "waterChart");
    removeData(tempChart, "tempChart");
    removeData(lightChart,"lightChart");
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
    //tempLevel = tempGuagePort;

}

function updateGraphs(){
    //update the graph with get graph info
    //lightgraph.append = lightlevel
    //watergraph.append = waterlevel
    //templevel.append = templevel
}