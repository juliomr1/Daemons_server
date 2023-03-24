import uasyncio as asyncio
from machine import Pin
import network 
import time
import urequests

p1 = Pin(2, Pin.OUT)
P2 = Pin(4, Pin.OUT)

async def daemon_wifi():
    wifi = network.WLAN(network.STA_IF)
    timeout = 0
    wifi.active(False)
    await asyncio.sleep(0.5)
    wifi.active(True)
    wifi.connect('TE VI PERRO','1083019146')
    while True:
        print("Daemon___0")
        if not wifi.isconnected():
            print('connecting...')
            while (not wifi.isconnected() and timeout < 5):
                # print(5 - timeout)
                 timeout = timeout + 1
                 await asyncio.sleep(1)
        if wifi.isconnected():
            print('connected')
        else:
            print('Not Connected')
        await asyncio.sleep(10)

loop = asyncio.get_event_loop()
loop.create_task(daemon_wifi())
#loop.create_task(daemon1())
loop.run_forever()
