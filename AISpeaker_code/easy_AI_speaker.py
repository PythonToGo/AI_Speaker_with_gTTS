import time, os 
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# Listening function (STT)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[Me]' + text)
        answer(text)
    except sr.UnknownValueError:
        print('cannnot recognize') # fail to recognize
    except sr.RequestError as e:
        print('fail to Request: {0}'.format(e))    # API Key Error, Netswork disconnection etc


# Answer
def answer(input_text): # Speaker talking:
    answer_text = ''
    if 'hello' in input_text:
        answer_text ='hello, Nice to meet you.'
    elif 'wheater' in input_text:
        answer_text = 'The temperature Munich today is 7 degree. It\'s cloudy and raining.'
    elif 'date' in input:
        answer_text = 'Today is September 29.'
    elif 'thank' in input_text:
        answer_text = 'you\'re welcome.'
    elif 'end' in input_text:
        anwer_text = 'See you again.'
        stop_listening(wait_for_stop=False) # End
    else:
        answer_text = 'Can you say it again?'
    speak(answer_text)

# 소리내어 읽기
def speak(text):
    print('[AI]' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text = text, lang = 'ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name): # Remove the file voice.mp3
        os.remove(file_name)

r = sr.Recognizer()
m = sr.Microphone()

speak('What can I do for you?')
stop_listening = r.listen_in_background(m, listen)
# stop_listening(wait_for_stop=False) # no more listen

while True:
    time.sleep(0.1)