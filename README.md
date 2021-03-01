#  **Real Time Sentiment Analyzer.**

Sentiment Analysis is a Natural Language Processing technique to predict the sentiment or opinion of a given text.
It involves the use of NLP, text analysis, computer linguistic to identify or extract subjective information. 


Sentiment Analysis is widely used to predict the sentiment of reviews, comments, survey responses, social media, etc.


A sentiment analyzer model can predict whether a given text refers to positive, negative, or neutral sentiment.
In this project my main focus is on developing a real-time sentiment analyzer, that can predict the sentiment of speech in real-time using open-sourced Python libraries such as NLTK and TextBlob.



### **Idea.**
In this project,  i developed a model that can listen to speech and convert it to text data, and use the **TextBlob** library to analyze the sentiment of the text in real-time.


1). Recognize the speech and convert it to text format using a speech recognizer engine.


2). Predict the sentiment of text using TextBlob in real-time.


3). Repeat steps 1 and 2 until the conversation ends. 

 
 ### **Installation.** 
 
 
 ##### **SpeechRecognition.**
 
 ~~~python
 pip install SpeechRecognition 
 ~~~ 
 
 ##### **pyforest**
 
 
 ~~~python
 pip install --upgrade pyforest
 ~~~
  
  
### **Source Code.**  

~~~python 
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
          
~~~
 
 

#### **Remember**

You can also implement the model in real-time using the above-discussed custom function, that will listen to your speech, and predict the sentiment.

In this experiment, i have used pre-trained sentiment classifier model from the TextBlob library. 

There are several other techniques to develop a sentiment analysis model.

[5 Ways to develop a Sentiment Analyser in Machine Learning By Satyam Kumar](https://towardsdatascience.com/5-ways-to-develop-a-sentiment-analyser-in-machine-learning-e8352872118)
