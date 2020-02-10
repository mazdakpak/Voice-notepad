from appJar import gui
import speech_recognition as sr 
import datetime
import random
import math
import winsound

def recordAudio():    
    # Record the audio
    r = sr.Recognizer()
    with sr.Microphone() as source:  
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        audio = r.listen(source)
    
    # Speech recognition using Google's Speech Recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        
    except sr.UnknownValueError:
        data = 'Google Speech Recognition could not understand'
    except sr.RequestError as e:
         data = 'Request error from Google Speech Recognition'
    return data
app = gui()
def btn():
    data = recordAudio()
    #app.stop()
    app.setTextArea('text' , data)
def clear():
    app.setTextArea('text' , " ")
  

app.addButton('Voice' , btn)
app.addButton('clean' , clear)
app.addTextArea("text")
app.go()