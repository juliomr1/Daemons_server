import serial
import time

ser = serial.Serial('COM5', 115200, timeout=1)

def run():
    ser.write(b'print("Hello, world!")\n')
    time.sleep(1)
    response = ser.read(9999)
    print(response.decode('utf-8'))

run()