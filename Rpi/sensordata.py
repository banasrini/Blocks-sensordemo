import os
import time
import sys
from pubnub import Pubnub
import Adafruit_DHT as dht

pubnub = Pubnub(publish_key='pub-c-6dbe7bfd-6408-430a-add4-85cdfe856b47', subscribe_key='sub-c-2a73818c-d2d3-11e3-9244-02ee2ddab7fe')

def printmess(message, channel):
    dict = message
    temp = dict['columns'][-1][-1]
    h,t = dht.read_retry(dht.DHT22, 4)
    tempF = (t*1.8) + 32
    pubnub.publish('tempeon', {
        'columns': [
            ['temperature', temp], #temperature from the Atmel microprocessor
            ['temp-pi', tempF] #temperature from the Pi
            ]
        })
    pubnub.publish('humeon', {
        'columns': [
            ['humidity', h] #humidity from the Pi
            ]

        })
    
pubnub.subscribe(channels = 'Atmel_Pubnub_2', callback = printmess);


    

#published in this fashion to comply with Eon
while True:
    h,t = dht.read_retry(dht.DHT22, 4)
    print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h)
    pubnub.publish('tempeon', {
        'columns': [
            ['temperature', temp]
            ]

        })
    pubnub.publish('humeon', {
        'columns': [
            ['humidity', h]
            ]

        })
