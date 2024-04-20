from flask import Flask
from flask import render_template
import time


#https://dev.to/alanjc/water-your-plant-using-a-raspberry-pi-and-python-2ddb
#https://projects.raspberrypi.org/en/projects/physical-computing/14
#https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/
#https://www.hackster.io/adhyoksh/controlling-gpio-pins-of-raspberry-pi-with-web-page-2d5bdc


app=Flask(__name__)

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

    return render_template('index.html')

if __name__ ==  '__main__':
    app.run(debug=True, host='0.0.0.0')