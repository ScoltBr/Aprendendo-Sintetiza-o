import pyttsx3

en = pyttsx3.init()
en.setProperty('rate', 125)
en.setProperty('valume', 0.50)
en.say("Olá Mundo, seja bem vindo")
en.setProperty('voice', b'brazil')
en.runAndWait()