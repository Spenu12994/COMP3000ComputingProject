# COMP3000ComputingProject
Githut repository for COMP3000's Computing Project

This is the repository for COMP3000 Personal Computing project for Spencer Underhill.
MAID is a Raspberry Pi running code that enables a local server and hardware intended for gathering sensor data from our components.

piServer.py - our main python file, this is the code that the MAID will be constantly running, and is the base template which server.py and hardware.py are built off of.

piServer uses the RPIO library that can only be run on the Raspberry Pi and not emulated on desktop. for the sake of testing and debugging, piServer has split its main components to server and hardware.
By this logic, the explanation of server.py and hardware.py is also the explanation for piServer.py.


server.py - the code that runs our server and manages our webpage. started by running the code with a python debugger (or in command line typing "sudo python3 server.py").
the server uses the flask library in order to host our server and handle requests.

using "@app.route('<address>')" we can run different functions based off of each address we have:

@app.route('/') - our index page, returns index.html
@app.route('/waterLevel') - function made for testing, this funtion returns "hello" and is used to debug serevr responses
@app.route('/lightLevel') - depricated function, would have been used to fetch the light level, but now we fetch all of the data at the same time
@app.route('/tempLevel') - depricated funciton, same intention as lightLevel:  would have been used to fetch the light level, but now we fetch all of the data at the same time
@app.route('/water') - this will complete the code to water our plants, then return a JSON variable containing the success state of the watering action
app.route('/values') - sends a json variable as a response which contains our 4 arrays (waterValues, tempValues, lightValues, xValues)
app.route('/update') - this function generates 3 mock values for our water, temp, and light variables, gets the current time, removes our oldest array value from each array, adds our new values to the top of the array, then responds with a JSON variable containing all of this information

finally "if __name__ == '__main__'" sets our server to start running.

servers are run off of localhost:5000. so all of these "routes" would follow 5000 like so: "localhost:5000/water" or "localhost:5000/update"


server.js uses templating to show our index page, and the folders "templates" and "static" achieve this.
within the template folder we have:

index.html - this html code initialises our buttons, classes for our charts, and calls the chart.js library, style.css file, and backend.js file.

style.css - sets the style of our html document. simple CSS that gives us some colour, sets our body border, customises the button, and adds an on hover animation for our water button to draw attention

backend.js - the file that handles all of the logic behind our index.html file. initialising our level variables, levels arrays, and localhost URL, then starting our createCharts function, which creates a chart for each of our sensor types using the arrays it gathers. next we initiate the page, onload we will fetch url + '/values' or localhost:5000/values, which we know will return all of the levels arrays stored on the server. we then take that data, convert it from a string to a JSON variable, then extract our arrays and pass them to our createCharts() function and initialise our local copies of our variables.

next addData function will add our new value to whichever array needs to be updated, and then updates our chart. removeData() does the same except removes our data instead of adding. 

updateCharts() will fetch our current values, add our data to our arrays using addData, remove our data from our arrays using removeData, and add and remove our time from the xValues array by pushing and shifting.

water() - fetches our water url (localhost:5000/water) which will tell our serever to water our plant and return a success message, we then await the message and log in the console if it was successful or not.

activate() - depricated function that was replaced by water(), this function would have turned on the device which was associated with the GPIO Pin number passed through.

updateWateringTimeFrame() - deprecated function kept in for the sake of future debugging or updating. this function was made with the intention to update the time on each sensor instance in the arrays on the local machine, and then send that back to the server, however by keeping our Raspberry Pi online, we can simply keep the time automatically update, leaving this function useless.

getGraphInfo, another depricated function which would fetch our information from the Pi using the /waterLevel /tempLevel /lightLevel routes, however these are depricated and so now is this function.
updateGraphs() would do the same as getGraphInfo, however send the data to the Pi instead of recieve.







hardware.py - the code that manages the components on the Raspberry Pi, and was used in testing as a "lite" version of our piServer, allowing us to test hardware was set up correctly without having to worry about fully configuring the server, or connecting over the internet.
importing os to run console commands, glob to read files, time to manage pump timings and analog reading, and RPI.GPIO: the Raspberry Pi library that allows us to communicate with hardware on the pins.

line 6 - initialises our variables for each component and its corresponding GPIO pin on the Raspberry Pi board (see wiring figures).

we set our mode to BCM and our moisture sensor as an input before configuring it...
to read our analog capacitive moisture sensor, we wait until the sensor is drained of electricity, then put power back into it and measure how long it takes for our power to read high.
this information is then used to determin the conductivity of our sensor, which can then be translated into a reading to measure the moisture in the soil.
analogRead() is a function used for testing purposes and as such is depricated in the final product.

our light sensor does not need any changing, and as such we can just set it up as an input.

our thermal sensor code starts by setting the temp sen as an input, then using console commands to use "modprove"... "w1-gpio" and "w1-therm" which activates our temperature sensor and allows it to start storing readings.
the thermal sensor is constantly reading information and outputs it to a file on the Raspberry Pi, so when we access it in our program we can simply read this file.
using glob, we can get the serial number of our device and search for it in our w1/devices folder, then run the w1_slave file to get our file.

read_temp_raw() opens our file and reads the lines before returning them,
read_temp() takes our raw lines, reads the lines that have "YES", then finds the line denoting our temperature. finally using string manipulation we extract the temperature from this string and divide it by 1000 to get our decimal points and temperature in celcius.

finally our main loop gets our moisture sensor readings, light sensor readings, temperature readings, and prints all of those out in that order. finally we replicate our pump using an LED by turning it on, sleeping for a second and then turning it off.
