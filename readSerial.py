import serial
import time

def SerialStart():
    serial_port = '/dev/ttyACM1'
    baud_rate = 9600
    data = 'data.dat'

    file = open(data, 'w+')
    ser = serial.Serial(serial_port, baud_rate)
    i = 0
    while i < 200:
        #ser.write('1'.encode())
        time.sleep(1)
        line = ser.readline()
        line = line.decode('utf-8')
        print(line)
        file.write(line)
        i = i + 1

SerialStart()