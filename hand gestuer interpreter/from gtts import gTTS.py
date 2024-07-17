from gtts import gTTS
import playsound
import os 
import serial

os.chdir(os.path.dirname(os.path.abspath(__file__)))
file = open('dictionary.txt','r')
arduino = serial.Serial(port='COM4',   baudrate=115200, timeout=.1)


def check_inter():
    data = arduino.readline()
    int(data)
    if data:
        return data

def sounnd(text):
    tts = gTTS(text=text , lang="ar")
    file_name = "interpreat.mp3"
    tts.save(file_name)
    playsound.playsound(file_name)    


while True:
    word_num = check_inter()
    content = file.readlines()
    linenumber = check_inter()
    inter = content[linenumber]
    sounnd(inter)
