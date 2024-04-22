from flask import Flask, render_template, jsonify, request, after_this_request
import time
import random #for mock data


#https://dev.to/alanjc/water-your-plant-using-a-raspberry-pi-and-python-2ddb
#https://projects.raspberrypi.org/en/projects/physical-computing/14
#https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/
#https://www.hackster.io/adhyoksh/controlling-gpio-pins-of-raspberry-pi-with-web-page-2d5bdc


app=Flask(__name__)

xValues = ["8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30"]
yValues = [7,8,8,9,9,9,10,11,14,14,15]
waterValues = [7,8,8,9,9,9,10,11,14,14,15]
tempValues = [23,24,22,20,24,25,19,21,23,22,24]
lightValues = [7,8,8,9,9,9,10,11,14,14,15]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/waterLevel')
def waterPage():
    #reading = RC_Analog(watSen)
    #waterLevel = reading
    return "Hello"

@app.route('/lightLevel')
def lightPage():
    #lightLevel = rpi.input(lighSen)
    return render_template('index.html')


@app.route('/tempLevel')
def tempPage():
    #tempLevel = read_temp()
    return render_template('index.html')

@app.route('/water')
def wateringPage():
    #code to water plants

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
    waterRand = random.randint(0,16)
    tempRand = random.randint(0,50)
    lightRand = random.randint(0,16)

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