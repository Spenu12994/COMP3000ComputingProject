from flask import Flask
from flask import render_template
from gpiozero import Motor
import os
import glob
import time
import RPI.GPIO as rpi
import time

#https://dev.to/alanjc/water-your-plant-using-a-raspberry-pi-and-python-2ddb
#https://projects.raspberrypi.org/en/projects/physical-computing/14
#https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/
#https://www.hackster.io/adhyoksh/controlling-gpio-pins-of-raspberry-pi-with-web-page-2d5bdc


app=Flask(__name__)

#setup pins
watSen, lighSen, tempSen, LEDPin = 22, 27, 17, 24

rpi.setwarning(False)
rpi.setmode(rpi.BOARD)

#rpi setup our water sensor and ligh sensor with their pins
rpi.setup(watSen, rpi.IN)

#https://github.com/jenfoxbot/SoilSensorAPI/blob/master/JenFoxBotSMSV1c.py

#same function as in the github page, modified to match our rpi library instead of the GPIO library
#function will discharge the sensor, run a current though, then calculate how much time it took to
#transmit enough voltage so our rpi reads it as high (meaning a lot has gone through)
#we can take this time it took to transmit in order to calculate how fast the voltage is 
#passing through, which in turn we can use to calculate how conductive our material is
def RC_Analog(Pin):
    counter=0
    start_time = time.time()
    #Discharge capacitor
    rpi.setup(Pin, rpi.OUT)
    rpi.output(Pin, rpi.LOW)
    time.sleep(0.1) #in seconds, suspends execution.
    rpi.setup(Pin, rpi.IN)
#Count loops until voltage across capacitor reads high on GPIO
    while (rpi.input(14)==rpi.LOW):
        counter=counter+1
    end_time = time.time()
    return end_time - start_time

#light sensor code https://www.uugear.com/portfolio/using-light-sensor-module-with-raspberry-pi/

rpi.setmode(rpi.BCM)

rpi.setup(lighSen, rpi.IN)

#temperature sensor
rpi.setup(tempSen, rpi.IN)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

#i am modifying this function from the original code to remove fareinheit, 
#as we can convert our farenheit at another point in the program to help with formatting our graphs.
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        #temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c
    
#change 7 and 14 for our pins
pump = Motor(7, 14)
#use commands like pump.forward() pump.backward(), pump.stop()

waterLevel = rpi.input(watSen)
lightLevel = rpi.input(lighSen)
tempLevel = rpi.input(tempSen)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/waterLevel')
def index():
    reading = RC_Analog(watSen)
    waterLevel = reading
    return render_template('index.html')

@app.route('/lightLevel')
def index():
    lightLevel = rpi.input(lighSen)
    return render_template('index.html')



#analogue light sensor
#from gpiozero import LightSensor

#@app.route('/lightLevelAnalogue')
#def index():
#    lightLevel = LightSensor(lighSen)
#    return render_template('index.html')


#https://www.youtube.com/watch?v=j7LLVkPpQ78

##type this on the raspberry pi to configure it with our temp sensor
#sudo nano /boot/config.txt
#dtoverlay=w1-gpio

#sudo modprobe w1-gpio
#sudo modprobe w1-therm

#cd /sys/bus/w1/devices/
#ls

###this code tests it is set up properly
#cd <serial number>
#ls
#cat w1_slave

#https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

@app.route('/tempLevel')
def index():
    tempLevel = read_temp();
    return render_template('index.html')

@app.route('/water')
def index():
    #code to water plants
    #pump.forward(0.5) #activate pump at half speed
    #sleep(5) #wait for 5
    #pump.stop() #stop the pump
    ##code to replicate with pump
    rpi.output(LEDPin, rpi.HIGH)
    time.sleep(5)
    rpi.output(LEDPin, rpi.LOW)
    return render_template('index.html')