import serial
import time

ser = serial.Serial('COM12')

commands = ['AT+A1', # Relay 1
            'AT+B1', # Relay 2
            'AT+C1', # Relay 3
            'AT+D1', # Relay 4
            'AT+E1', # Relay 5
            'AT+F1', # Relay 6
            'AT+G1', # Relay 7
            'AT+H1', # Relay 8
            'AT+I1', # Relay 9
            'AT+J1', # Relay 10
            'AT+K1', # Relay 11
            'AT+L1', # Relay 12
            'AT+M1', # Relay 13
            'AT+N1', # Relay 14
            'AT+O1', # Relay 15
            'AT+P1'] # Relay 16

for command in commands:
    ser.write(bytes(command, encoding='ascii') )
    time.sleep(0.1)