from flask import Flask
from flask import render_template
from gpiozero import Motor
import RPI.GPIO as rpi
import time

#https://dev.to/alanjc/water-your-plant-using-a-raspberry-pi-and-python-2ddb
#https://projects.raspberrypi.org/en/projects/physical-computing/14
#https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/
#https://www.hackster.io/adhyoksh/controlling-gpio-pins-of-raspberry-pi-with-web-page-2d5bdc


app=Flask(__name__)

#setup pins
watSen, lighSen, tempSen= 3, 5, 1

rpi.setwarning(False)
rpi.setmode(rpi.BOARD)

#rpi setup our water sensor and ligh sensor with their pins
rpi.setup(watSen, rpi.IN)
rpi.setup(lighSen, rpi.IN)
rpi.setup(tempSen, rpi.IN)

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
    waterLevel = rpi.input(watSen)
    return render_template('index.html')

@app.route('/lightLevel')
def index():
    lightLevel = rpi.input(lighSen)
    return render_template('index.html')

@app.route('/tempLevel')
def index():
    tempLevel = rpi.input(tempSen)
    return render_template('index.html')

@app.route('/water')
def index():
    #code to water plants
    pump.forward(0.5) #activate pump at half speed
    sleep(5) #wait for 5
    pump.stop() #stop the pump

    return render_template('index.html')