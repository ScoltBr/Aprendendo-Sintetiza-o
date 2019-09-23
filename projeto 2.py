from gtts import gTTS
from pygame import mixer
import os.path

diretorio = input('Digite o Diretorio do arquivo de texto.')

teste = os.path.isfile(diretorio) #Ira ver se o realmente é um arquivo e vai retornar true or false

if teste == True:
    print("O Arquivo esta sendo carregado, Aguarde ")
    file_data = open(diretorio) #Vai abrir o arquivo que esta no diretorio
    file_data = file_data.read() #E ira ler o arquivo

    voz = gTTS(file_data, lang='PT')
    voz.save('arquivo1.mp3')
    print("Falando...")

    mixer.init()
    mixer.music.load('arquivo1.mp3')
    mixer.music.play()

else:
    print("Diretorio Não encontrado")
