import serial
import time

ser = serial.Serial('COM4', 9600, timeout=500)
while True:
    x = input('Enter command: ')
    x += '\n'
    data = serial.to_bytes(x.encode())
    ser.write(data)
    val = ser.readline()
    if len(val) > 0:
        print(val.decode('utf-8'))