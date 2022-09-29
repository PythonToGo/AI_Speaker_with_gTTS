# TTS (Text To Speech)

from gtts import gTTS
from playsound import playsound

text = '안녕하세요.'
file_name = 'tts_complete_kor.mp3'
tts_ko = gTTS(text = text, lang = 'ko')
tts_ko.save(file_name)
playsound(file_name) # .mp3 file play

# long Sentense
with open('tts_complete_kor.txt', 'r', encoding ='utf8') as f:
    text = f.read()