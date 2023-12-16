let lightLevel = 0;
let waterLevel = 0;
let pressureLevel = 0;

let lightGuagePort = 1;
let waterGuagePort = 2;
let pressureGuagePort = 3;
let pumpPort = 4;

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