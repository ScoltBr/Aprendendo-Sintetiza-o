import speech_recognition as sr

recom = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga Algo")
    audio = recom.listen(source)

print(recom.recognize_sphinx(audio))