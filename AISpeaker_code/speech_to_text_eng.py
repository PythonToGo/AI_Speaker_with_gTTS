# STT (Speech To Text)

import speech_recognition as sr

### listen to the Microphone ###
r = sr.Recognizer()
with sr.Microphone() as source:
    print('I am listening')
    audio = r.listen(source) #listen with Microphone

### import audio from file (wav, aiff, flac) >> cannot use .mp3 ##
# r = sr.Recognizer()
# with sr.AudioFile('sample.wav') as source:
#     audio = r.record(source)

# Exceptional Case
try:
    text = r.recognize_google(audio, language= 'en-US') # Google API Recognition max. 50/day
    print(text)

except sr.UnknownValueError:
    print('cannnot recognize') # fail to recognize
except sr.RequestError as e:
    print('fail to Request: {0}'.format(e))    # API Key Error, Netswork disconnection etc

