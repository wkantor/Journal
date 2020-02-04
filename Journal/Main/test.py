'''
Created on 4 Feb 2020

@author: VojtechK
'''

from datetime import datetime
from tkinter import *
from tkinter.filedialog import *


def raise_frame(frame):
    frame.tkraise()
# Nadzdzwignie dany frame nad tyn przedtym


def saveFile(text):
    file_name = asksaveasfilename(defaultextension=".txt",
                                  filetypes=[("All Files", "*.*"),
                                             ("Text Documents", "*.txt")])
    if file_name:
        f = open(file_name, 'w')
        contents = text.get(1.0, 'end')
        f.write(contents)
        f.close()
# function which saves files


def combine(a1, a2, a3, a4, a5, a6):
    file_name = asksaveasfilename(defaultextension=".txt",
                                  filetypes=[("All Files", "*.*"),
                                             ("Text Documents", "*.txt")])
    if file_name:
        f = open(file_name, 'w')
        contents = "STATEMENT\n" + a1.get(1.0, 'end') + "\n\n" + \
                   "IS IT TRUE?\n" + a2.get(1.0, 'end') + "\n\n" + \
                   "IS IT REALLY TRUE?\n" + a3.get(1.0, 'end') + "\n\n" + \
                   "HOW DO YOU FEEL?\n" + a4.get(1.0, 'end') + "\n\n" + \
                   "WHO WOULD YOU BE?\n" + a5.get(1.0, 'end') + "\n\n" + \
                   "TURNAROUND\n" + a6.get(1.0, 'end')
        f.write(contents)
        f.close()
# combine texts from the work into one


root = Tk()
root.attributes("-fullscreen", True)   # fulscreen mode
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# zrobi colimny a rowy (kiere mi tworzom, grid - pracujom z framami) wileki


def generuj_strone():
    x = Frame(root, background='black',)
    x.grid(row=0, column=0, sticky='news')
    return x


def generuj_gnapis(frame, text):
    x = Label(frame, text=text, font=(
        "arial", 30, "bold"), fg='white', bg='black')
    x.place(relx=0.5, rely=0.1, anchor=CENTER)
    return x


def generuj_button(frame, text, command, relx, rely, anchor):
    x = Button(frame, text=text,
               command=lambda: command)
    x.place(relx=relx, rely=rely, anchor=anchor)
    return x


f1 = generuj_strone()
f2 = generuj_strone()
n1 = generuj_gnapis(f1, "welcome")
n2 = generuj_gnapis(f2, "f2")
b1 = generuj_button(f1, "f2", raise_frame(f2), 0.1, 0.1, CENTER)


raise_frame(f1)
root.mainloop()
