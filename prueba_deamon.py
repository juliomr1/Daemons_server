import uasyncio as asyncio
from machine import Pin
import network 


p1 = Pin(2, Pin.OUT)
P2 = Pin(4, Pin.OUT)

async def daemon():
    while True:
        print("Daemon___0")
        p1.on()
        await asyncio.sleep_ms(100)
        p1.off()
        #time.sleep_ms(50)
        await asyncio.sleep(1)

async def daemon1():
    while True:
        print("Daemon___1")
        P2.on()
        await asyncio.sleep_ms(100)
        P2.off()
        await asyncio.sleep(2)


loop = asyncio.get_event_loop()
loop.create_task(daemon())
loop.create_task(daemon1())
loop.run_forever()
