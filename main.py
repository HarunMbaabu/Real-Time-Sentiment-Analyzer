import speech_recognition as sr
import nltk

r = sr.Recognizer()
while True:
  with sr.Microphone() as source:
      print('Say Something...')
      audio = r.listen(source, timeout=2)
      try:
          text = r.recognize_google(audio)
          if lower(str(text)) == "Exit":
            break
          tb = blob(text)
          print(text)
          print(tb.sentiment)
      except:
          print('Try again')