from tkinter import *
from nltk.corpus import wordnet
import pyttsx3

root=Tk()
root.title("Dictionary")
root.geometry('320x140')
w=Entry(root)
w.pack(fill=X)
l=Label(root)
mean=""
def speech():
    global mean
    engine=pyttsx3.init()
    engine.say(mean)
    engine.runAndWait()
def dic():
    global l,w,mean
    word=w.get()
    syn=wordnet.synsets(word)[0]
    mean=syn.definition()
    example=syn.examples()
    if(example):
       mean+='\n'+"examples:"
       for sent in example:
           mean+='\n'+sent
    l.config(text=mean)
b=Button(root,text="search",command=dic)
b2=Button(root,text="speak",command=speech)
b.pack()
b2.pack()
l.pack()

root.mainloop()
