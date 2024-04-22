let lightLevel = 0;
let waterLevel = 0;
let tempLevel = 0;

let lightGuagePort = 1;
let waterGuagePort = 2;
let tempGuagePort = 3;
let pumpPort = 4;

const url = 'http://localhost:5000/'


xValues = [];
const yValues = [7,8,8,9,9,9,10,11,14,14,15];
waterValues = [];
tempValues = [];
lightValues = [];



function createCharts(waterArray, tempArray, lightArray, xValues){
  waterChart = new Chart(document.getElementById("waterChart"), {
      type: "line",
      data: {
        labels: xValues,
        datasets: [{
          fill: false,
          lineTension: 0,
          backgroundColor: "rgba(0,0,255,1.0)",
          borderColor: "rgba(0,0,255,0.1)",
          data: waterArray
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

  tempChart = new Chart("tempChart", {
      type: "line",
      data: {
        labels: xValues,
        datasets: [{
          fill: false,
          lineTension: 0,
          backgroundColor: "rgba(0,0,255,1.0)",
          borderColor: "rgba(0,0,255,0.1)",
          data: tempArray
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

  lightChart = new Chart("lightChart", {
      type: "line",
      data: {
        labels: xValues,
        datasets: [{
          fill: false,
          lineTension: 0,
          backgroundColor: "rgba(0,0,255,1.0)",
          borderColor: "rgba(0,0,255,0.1)",
          data: lightArray
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
}

//Initiate Page
fetch(url + '/values')
.then(response=>response.json())
.then(json =>{
      console.log(json);
      console.log(JSON.stringify(json));
      createCharts(json.water, json.temp, json.light, json.xVals)
      waterValues = json.water;
      tempValues = json.temp;
      lightValues = json.light;
      xValues = json.xVals;
})



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

 

 


function updateCharts(){//this should update with our data reading hardware every alloted time frame (such as every 30 minutes)
    fetch(url + '/update')
    .then(response=>response.json())
    .then(json =>{
    
    var currTimeText = json.time;

    xValues.push(currTimeText);
    xValues.shift();

    addData(waterChart, "waterChart", json.water); //math.random is used to simulate a response from our hardware, once implemented our data values from hardware will be inputted here instead
    addData(tempChart, "tempChart", json.temp);
    addData(lightChart,"lightChart", json.light);

    
    removeData(waterChart, "waterChart");
    removeData(tempChart, "tempChart");
    removeData(lightChart,"lightChart");
  })
}




function water(){
    const waterUrl = url + '/water'
    fetch(waterUrl)
    .then(response=>response.json())
    .then(json =>{
      console.log(json);
      console.log(JSON.stringify(json));

      if (json.success == 'yes'){
        console.log("Watered Successfully");
      }
      else{
        console.log("Watering Failed");
      }
    })
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