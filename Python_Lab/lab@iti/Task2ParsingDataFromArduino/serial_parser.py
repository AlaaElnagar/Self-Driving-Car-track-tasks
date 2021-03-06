import serial
import time
import csv

ser = serial.Serial('/dev/ttyACM0')
ser.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8")) #"utf-8" to decode
        print(decoded_bytes)
        with open("Ultrasonic_readings.csv","a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([time.time(),decoded_bytes])  #show result with time 
    except:
        print("Keyboard Interrupt") 
        break
