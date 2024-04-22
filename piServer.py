from flask import Flask, render_template, jsonify, request, after_this_request
import time
import random #for mock data
import os
import glob
import time
import RPi.GPIO as rpi

#https://dev.to/alanjc/water-your-plant-using-a-raspberry-pi-and-python-2ddb
#https://projects.raspberrypi.org/en/projects/physical-computing/14
#https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/
#https://www.hackster.io/adhyoksh/controlling-gpio-pins-of-raspberry-pi-with-web-page-2d5bdc


##############################


watSen, lighSen, tempSen, LEDPin = 14,27,4,24

rpi.setmode(rpi.BCM)
rpi.setup(watSen,rpi.IN)

#Moisture Sensor

def RC_Analog(Pin):
    counter=0
    start_time = time.time()
    rpi.setup(Pin, rpi.OUT)
    rpi.output(Pin, rpi.LOW)
    time.sleep(0.1)
    rpi.setup(Pin, rpi.IN)
    while(rpi.input(Pin)==rpi.LOW):
        counter=counter+1
    end_time = time.time()
    return end_time - start_time
def analogRead(Pin):
    soilMoisture = analogRead(A0)

#light Sen
    
rpi.setup(lighSen,rpi.IN)

#temp Sen
rpi.setup(tempSen,rpi.IN)
#turns on our thermal sensor from the console
#the thermal probe constantly grabs data even while the application is off,
#we simply use the application to grab the data its already collected
os.system('modprove w1-gpio')
os.system('modprobe w1-therm')

#file the serial number of our device
base_dir = 'sys/bus/w1/devices'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, "r")
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equal_pos = lines[1].find('t=')
    if equal_pos != -1:
        temp_string = lines[1][equal_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
 
       
        





#############################





app=Flask(__name__)

xValues = ["8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30"]
yValues = [7,8,8,9,9,9,10,11,14,14,15]
waterValues = [7,8,8,9,9,9,10,11,14,14,15]
tempValues = [23,24,22,20,24,25,19,21,23,22,24]
lightValues = [7,8,8,9,9,9,10,11,14,14,15]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/water')
def wateringPage():
    #code to water plants
    rpi.output(LEDPin, rpi.HIGH)
    time.sleep(1)
    rpi.output(LEDPin, rpi.LOW)
    response = {'response': 'water', 'success' : 'yes'}
    print(response)
    return jsonify(response)

@app.route('/values')
def returnValues():
    #code to water plants

    response = {'response': 'values', 'water' : waterValues, 'temp' : tempValues, 'light' : lightValues, 'xVals' : xValues} 
    print(response)
    return jsonify(response)


@app.route('/update')
def returnUpdate():
    #code to water plants

    reading = RC_Analog(watSen)
    
    print("Water Level =", reading)

    waterRand = reading

    tempLevel = read_temp()
    print("Temp Level =", tempLevel, ".C")
    tempRand = tempLevel

    lightLevel = rpi.input(lighSen)
    print("Light Level = ", lightLevel)#0 if bright enough, 1 if not

    lightRand = lightLevel

    current_time = time.localtime()
    hourMinute = str(current_time.tm_hour).zfill(2) + ":" + str(current_time.tm_min).zfill(2)

    waterValues.pop(0)
    tempValues.pop(0)
    lightValues.pop(0)
    xValues.pop(0)

    waterValues.append(waterRand)
    tempValues.append(tempRand)
    lightValues.append(lightRand)
    xValues.append(hourMinute)

    response = {'response': 'values', 'water' : waterRand, 'temp' : tempRand, 'light' : lightRand, 'time' : hourMinute} 
    print(response)
    return jsonify(response)

if __name__ ==  '__main__':
    app.run(debug=True, host='0.0.0.0')