import pygame
from pygame import mixer
from tkinter import *
import os

#Intializing the buttons

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()    

root=Tk()
root.title('MP3 Music Player__')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#Input Taking List of Music

playlist=Listbox(root,selectmode=SINGLE,bg="pink",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)

os.chdir(r'E:\IT  VEDANT\UNIcompiler intership\Sample or project\proxlight')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="PLAY",command=playsong)
playbtn.config(font=('arial',20),bg="Orange",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="PAUSE",command=pausesong)
pausebtn.config(font=('arial',20),bg="Orange",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="STOP",command=stopsong)
stopbtn.config(font=('arial',20),bg="Orange",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="RESUME",command=resumesong)
Resumebtn.config(font=('arial',20),bg="Orange",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)


mainloop()