import pyttsx3
from datetime import  datetime

agora = datetime.now()

nome = "Nome"
hora = agora.hour
minuto = agora.minute

texto = "Olá " + str(nome) + " sejá bem vindo, agora são " + str(hora) + " horas e " + str(minuto) + " minutos"

en = pyttsx3.init()
en.setProperty('rate', 125)
en.setProperty('valume', 0.5 )
en.setProperty('voice', b'brazil')
en.say(texto)
en.runAndWait()