import serial
from re import search
import pyautogui

#Configuration 
port = "COM1"
baud_rate = 9600

arduino = serial.Serial(port, baud_rate)
arduino.connect()

if arduino.isOpen():
	arduino.write("start".encode())
	i = 1
	position = []
	while True:
		s = search("[0-9]",str(arduino.readline()))
		position.append(int(s.group(0)))
		if i%2 == 0:
			if position[0] and position[1]:
				pyautogui.moveRel(position[0], position[1])
				position = []	
		i+=1
