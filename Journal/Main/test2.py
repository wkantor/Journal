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


class Strona:
    def __init__(self):
        self.frame = Frame(root, background='black',)

    def frame(self):
        return self.frame.grid(row=0, column=0, sticky='news')


class Napis:
    def napis(self, frame, txt):
        self.napis = Label(frame, text=txt, font=(
            "arial", 30, "bold"), fg='white', bg='black')
        return self.napis.place(relx=0.1, rely=0.1, anchor=CENTER)


S1 = Strona()
F1 = S1.frame
F2 = S1.frame

N1 = Napis()
Gn1 = N1.napis(F1, "Witej")


raise_frame(F1)
root.mainloop()
