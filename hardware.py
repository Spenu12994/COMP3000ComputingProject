import os
import glob
import time
import RPi.GPIO as rpi

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
    
#main loop
    while(True):
        reading = RC_Analog(watSen)
        waterLevel = reading
        print("Water Level =", waterLevel)

        lightLevel = rpi.input(lighSen)
        print("Light Level = ", lightLevel)#0 if bright enough, 1 if not

        tempLevel = read_temp()
        print("Temp Level =", tempLevel, ".C")
        rpi.output(LEDPin, rpi.HIGH)
        time.sleep(1)
        rpi.output(LEDPin, rpi.LOW)