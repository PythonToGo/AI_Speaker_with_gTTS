# TTS (Text To Speech)

from gtts import gTTS
from playsound import playsound

text = 'How can I help you?'
file_name = 'tts_complete_eng.mp3'
tts_en = gTTS(text=text, lang='en')
tts_en.save(file_name) 
playsound(file_name) # .mp3 file play


# long Sentense
with open('tts_complete_eng.txt', 'r', encoding ='utf8') as f:
    text = f.read()