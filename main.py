import time
import grovepi

# Connect the Grove Light Sensor to analog port A0
light_sensor = 0

grovepi.pinMode(light_sensor,"INPUT")

while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(light_sensor)

        print("sensor_value =", sensor_value)
        time.sleep(.5)

    except IOError:
        print ("Error")

