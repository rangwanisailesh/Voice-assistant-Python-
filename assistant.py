import pyttsx3
import speech_recognition as sr
import webbrowser
from googlesearch import search

e=pyttsx3.init()

def searchcheck():
        r=sr.Recognizer()
        with sr.Microphone() as source:
                print("Assistant: Google or wikipedia")
                e.say("Can i search this on google or you want to get information from wikipedia?")
                e.runAndWait()
                audio=r.listen(source)
                abc=r.recognize_google(audio)
                print("You: "+abc)
                if(abc=="Google" or abc=="search from google" or abc=="from google" or abc=="google search"):
                        search="www.google.com/search?q="
                        webbrowser.open(search+abc)
                        ai='Here are the results on google, what you want to know.'
                        e.say(ai)
                        e.runAndWait()
                        recognize()
                elif(abc=="wikipedia" or abc=="Wiki" or abc=="search from wikipedia" or abc=="from wikipedia" or abc=="wikipedia search"):
                        search="https://en.wikipedia.org/wiki/"
                        webbrowser.open(search+abc)
                        ai='Here are the results on wikipedia, what you want to know.'
                        e.say(ai)
                        e.runAndWait()
                        recognize()
                elif(abc=="back" or abc=="go back"):
                        return recognize()
                else:
                        e.say("Sorry boss, I did not get it. Can you say that again?")
                        e.runAndWait()
                        searchcheck()

def recognize():
        r=sr.Recognizer()
        with sr.Microphone() as source:
                print("\n"+"Say Something!")
                audio=r.listen(source)
                a=r.recognize_google(audio)
                print("You: "+a)
                words=a
                if(words=='what can you do for me'):
                        ai="I can search from web anything you want to know."
                        e.say(ai)
                        print("Assistant: "+ai)
                        e.runAndWait()
                        recognize()
                elif(words=='how are you' or words=="how' you"):
                        ai="I am good, what about you boss?"
                        e.say(ai)
                        print("Assistant: "+ai)
                        e.runAndWait()
                        recognize()
                elif(words=="bye" or words=="goodbye" or words=="goodbye goodbye" or words=="good bye" or words=='exit' or words=='quit'):
                        ai="If you need me then I am always available for you. Have a good day!"
                        e.say(ai)
                        print("Assistant: "+ai)
                        e.runAndWait()
                        quit()
                elif(words=='who made you'):
                        ai="Sailesh Rangwani is the one who wrote me as a program."
                        e.say(ai)
                        print("Assistant: "+ai)
                        e.runAndWait()
                        recognize()
                elif(words=='describe yourself' or words=='who are you' or words=='who is your owner'):
                        ai="I am a program written by Sailesh Rangwani, whom i called him a boss."
                        e.say(ai)
                        print("Assistant: "+ai)
                        e.runAndWait()
                        recognize()
                elif(words==None or words==0):  
                        recognize()
                else:
                        r=sr.Recognizer()
                        with sr.Microphone() as source:
                                print("Assistant: Google or wikipedia")
                                e.say("Can i search this on google or you want to get information from wikipedia?")
                                e.runAndWait()
                                audio=r.listen(source)
                                abc=r.recognize_google(audio)
                                print("You: "+abc)
                                if(abc=="Google" or abc=="Search from google" or abc=="From google" or abc=="Google search"):
                                        search="www.google.com/search?q="
                                        webbrowser.open(search+words)
                                        ai='Here are the results on google, what you want to know.'
                                        e.say(ai)
                                        e.runAndWait()
                                        recognize()
                                elif(abc=="Wikipedia" or abc=="Wiki" or abc=="Search from wikipedia" or abc=="From wikipedia" or abc=="Wikipedia search"):
                                        search="https://en.wikipedia.org/wiki/"
                                        webbrowser.open(search+words)
                                        ai='Here are the results on wikipedia, what you want to know.'
                                        e.say(ai)
                                        e.runAndWait()
                                        recognize()
                                elif(abc=="back" or abc=="go back"):
                                        recognize()
                                else:
                                        e.say("Sorry boss, I did not get it. Can you search that again?")
                                        e.runAndWait()
                                        recognize()

def activation():
        r=sr.Recognizer()
        with sr.Microphone() as source:
                audio=r.listen(source)
                ab=r.recognize_google(audio)
                activate=ab
                if(activate=="activate"):
                        print("\t\tSailesh Assistant\n")
                        e.say("Hello boss! I am activated")
                        e.runAndWait()
                        recognize()
                else:
                        e.say("Sorry, you are not able to activate me. Try again.")
                        e.runAndWait()
                        activation()
        
e.say("Hello there! Activate me!")
e.runAndWait()
activation()

