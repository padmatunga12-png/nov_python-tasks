

from gtts import gTTS
sample = "welcome to pythonlife hi everyone"
tts = gTTS('sample', lang='en')
tts.save('hello.mp3')
