# -*- coding: utf-8 -*-


import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import requests
import json

listener= sr.Recognizer()

engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)


def engineTalk(text):
    engine.say(text)
    engine.runAndWait()
    
    
engine.say("i am alexa. how can i help you ?")
engine.runAndWait()

def userCommands():
    try:
        with sr.Microphone() as source:
            print("start speaking")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command


def weather(city):
   
    api_key = 'ed94b80d565b5eb621110d55564066c5'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"   
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    response = requests.get(complete_url) 
    x = response.json() 
    if x["cod"] != "404": 
        
            y = x["main"] 
            current_temperature = y["temp"] 
        
    
    

def runAlexa():
    command=userCommands()
    if 'play' in command:
        song=command.replace('play','')
        engineTalk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time now' in command:
        time=datetime.datetime.now().strftime('%H:%M:%S')
        engineTalk('current time is '+ time)
    elif 'your name' in command:
        engineTalk('My name is Alexa')
    elif 'what is' in command:
        name =command.replace('who is','')
        info=wikipedia.summary(name,1)
        engineTalk(info)
    elif 'joke' in command:
        engineTalk(pyjokes.get_joke())
    elif 'weather' in command:
        engineTalk("name of the city")
        city=userCommands()
        weatherAPI=weather(city)
        engineTalk(weatherAPI + 'degree farenheit')
    elif 'message' in command:
        engineTalk("enter the number")
        num=userCommands()
        print(str(num))
        engineTalk("what is your message")
        msg=userCommands()
        print(msg)
        engineTalk("specify the time. hours?")
        hrs=userCommands()
        print(hrs)
        engineTalk("minutes?")
        mins=userCommands()
        print(mins)
        pywhatkit.sendwhatmsg(f"+91{num}",msg,int(hrs),int(mins))
        engineTalk("messsage sent")
    elif 'stop alexa' in command:
        sys.exit()
    else:
        engineTalk('I could not hear you properly')
        


while True:
    runAlexa()
                 