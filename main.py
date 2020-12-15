# recognise speech
import speech_recognition as sr
# get time details
from time import ctime 
# open browser
import webbrowser 
import time
# to remove created audio files
import os
import playsound
import random
from gtts import gTTS

# initialise a recogniser
r = sr.Recognizer()
# listen for audio and convert it to text
def record_audio( ask = False ):
    # microphone as source
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        # listen for the audio via source
        audio = r.listen(source) 
        voice_data = ''
        try:
            # convert audio to text
            voice_data = r.recognize_google(audio)
            print(voice_data)
        # error: recognizer does not understand
        except sr.UnknownValueError:
            alexis_speak('Sorry, i did not get that')
        # error: recognizer is not connected
        except sr.RequestError:
            alexis_speak('Sorry, my speech service is down')
        return voice_data

# get string and make a audio file to be played
def alexis_speak(audio_string):
    # text to speech (voice)
    tts = gTTS(text = audio_string, lang = 'en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('My name is Alexis')

    if 'what time is it' in voice_data:
        alexis_speak(ctime())

    if 'search' in voice_data:
        search = record_audio('what do you want to search')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Here is what i found for ' + search)

    if 'find location' in voice_data:
        location = record_audio('what is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Here is the location of ' + location)

    if 'exit' in voice_data:
        exit()

time.sleep(1)

alexis_speak('how can i help you?')
while 1:
    # get the voice input
    voice_data = record_audio()
    # respond
    respond(voice_data)