import pygame
import os
import tkinter as tkr
from tkinter.filedialog import askdirectory

musicplayer = tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry('900x500')

directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer,font="Helvetica 12 bold",bg="yellow",selectmode=tkr.SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos,item)
    pos = pos + 1


pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def ExitMusicPlayer():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def fadeout():
    pygame.mixer.music.fadeout(5000)


button1 = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",bg="red",fg="white",text="PLAY",command=play)
button2 = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",bg="purple",fg="white",text="STOP",command=ExitMusicPlayer)
button3 = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",bg="orange",fg="white",text="PAUSE",command=pause)
button4 = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",bg="blue",fg="white",text="UNPAUSE",command=unpause)
button5 = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",bg="blue",fg="white",text="FADEOUT",command=fadeout)


var = tkr.StringVar()
songtitle = tkr.Label(musicplayer,font="Helvetica 12 bold",textvariable=var)

songtitle.pack()
button1.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
button2.pack(fill="x")
button5.pack(fill="x")
playlist.pack(fill="both",expand="yes")

musicplayer.mainloop()
