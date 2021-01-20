from machine import Pin
from machine import PWM
import time
import dimmer
import sensor_ultrasonic
import network
import time

id="pir"                                                                        #device id pir/ultra/light

#connect to wifi
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect('wifi', auth=(network.WLAN.WPA2, 'password'))                      #wifi name and password
while not wlan.isconnected():
    time.sleep_ms(50)
print("Connected")

#setup pir sensor on pin 14
pir = Pin('P14',mode=Pin.IN, pull=Pin.PULL_UP)

current_time = 0

#setup callback
io=0
def sub_cb(topic, msg):
    global io
    print(": ",msg)
    if msg==b'1':
        io=1
    elif msg==b'0':
        io=0

#connect to mqtt server
def connect_mqtt():
    global client
    from mqtt import MQTTClient
    client = MQTTClient(id, "mqtt",user="user",password="password",port=1883)    
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic="Lights/feeds/"+id)                                                  

connect_mqtt()

#main loop
while True:
    if pir() == 1: #or sensor_ultrasonic.distance_measure(20) == True           check sensor
        client.publish(topic="Lights/feeds/ultra",msg="1")                      #send 1 to other light
        client.publish(topic="Lights/feeds/light",msg="1")                      #send 1 to other light
        client.publish(topic="Lights/feeds/pir",msg="1")                        #send 1 to other light

        dimmer.dimmer("P8",1)                                                   #start led on max
        current_time = time.time()
        time.sleep(1)
    if time.time() > current_time + 5:
        if time.time() > current_time + 10:
            dimmer.dimmer('P8',0)                                               #after 10 sec turn off light
            time.sleep(1)
        else:
            dimmer.dimmer("P8",0.01)                                             #after 5 turn down light
            time.sleep(1)
    client.check_msg()
    if time.time() > current_time + 5 and io ==1 :                              #if light is not max and other sensor sends 1
        current_time = time.time()
        dimmer.dimmer("P8",0.01)                                                 #turn on low light
        time.sleep(1)
        client.publish(topic="Lights/feeds/"+id,msg="0")                        #send 0 to own feed
