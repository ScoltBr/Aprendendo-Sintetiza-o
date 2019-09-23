from gtts import gTTS
from pygame import mixer


voz = gTTS("Olá, vamos sintetizar com voz python", lang='PT')
voz.save("voz.mp3")

mixer.init()
mixer.music.load('voz.mp3')
mixer.music.play()

x = input('Digite algo para Finalizar...')
