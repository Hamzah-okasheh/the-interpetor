from gtts import gTTS
import playsound
import os 
import serial

os.chdir(os.path.dirname(os.path.abspath(__file__)))
file = open('dictionary.txt')
arduino = serial.Serial(port='COM4',   baudrate=115200, timeout=.1)


def check_inter():
    data = arduino.readline()
    int(data)
    if data:
        return data
    

while True:
    dictnum = check_inter()
