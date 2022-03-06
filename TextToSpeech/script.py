import pyttsx3
import os
engine = pyttsx3.init() # object creation

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', input(''))   #changing index, changes voices. 1 for female

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
                      
engine.setProperty('rate', input(''))     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
                        
engine.setProperty('volume',input(''))    # setting up volume level  between 0 and 1


#engine.say(input(""))
string =input("")
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed

engine.save_to_file(string, 'speech.mp3')


engine.runAndWait()