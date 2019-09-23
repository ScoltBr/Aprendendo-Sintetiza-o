import pyttsx3

en = pyttsx3.init()

nova_velocidade = 50
while nova_velocidade <= 300:
    en.setProperty('rate', nova_velocidade)
    en.say("Testando a velocidade")
    en.runAndWait()
    nova_velocidade += 50