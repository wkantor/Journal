'''
Created on 4 Feb 2020

@author: VojtechK
'''

from datetime import datetime
from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.attributes("-fullscreen", True)   # fulscreen mode
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# zrobi colimny a rowy (kiere mi tworzom, grid - pracujom z framami) wileki


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


def lista_c():
    y = []
    with open('contemplation.txt', 'r') as file:
        for a in file:
            x = a.replace('\n', '')
            y.append(x)
    return y


def lista_q():
    y = []
    with open('quotes.txt', 'r') as file:
        for a in file:
            x = a.replace('\n', '')
            y.append(x)
    return y


def generuj_strone():
    x = Frame(root, background='black',)
    x.grid(row=0, column=0, sticky='news')
    return x


def generuj_gnapis(frame, text):
    x = Label(frame, text=text, font=(
        "arial", 30, "bold"), fg='white', bg='black')
    x.place(relx=0.5, rely=0.1, anchor=CENTER)
    return x


def generuj_napis(frame, text, relx, rely, anchor):
    x = Label(frame, text=text, fg='white', bg='black')
    x.place(relx=relx, rely=rely, anchor=anchor)
    return x


def generuj_button_cf(frame, text, f, relx, rely, anchor):
    x = Button(frame, text=text, command=lambda: raise_frame(f))
    x.place(relx=relx, rely=rely, anchor=anchor)
    return x


def generuj_button_s(frame, text, t, relx, rely, anchor):
    x = Button(frame, text=text, command=lambda: saveFile(t))
    x.place(relx=relx, rely=rely, anchor=anchor)
    return x


def generuj_button_s_a(frame, text, a1, a2, a3, a4, a5, a6, relx, rely, anchor):
    x = Button(frame, text=text, command=lambda: combine(
        a1, a2, a3, a4, a5, a6))
    x.place(relx=relx, rely=rely, anchor=anchor)
    return x


def generuj_button_q(frame, text, relx, rely, anchor):
    x = Button(frame, text=text, command=lambda: quit())
    x.place(relx=relx, rely=rely, anchor=anchor)
    return x


def generuj_text(frame, height, width, relx, rely, anchor, insert):
    x = Text(frame, height=height, width=width)
    x.place(relx=relx, rely=rely, anchor=anchor)
    x.insert(END, insert)
    return x
# funkcje, kiere generujom potrzebne widgety


f1 = generuj_strone()
f2 = generuj_strone()
f3 = generuj_strone()
f4 = generuj_strone()
f5 = generuj_strone()
# Okna

###
###
###


n1 = generuj_gnapis(f1, "Welcome to the Journal!")
b11 = generuj_button_cf(f1, "Free writing", f2, 0.1, 0.2, CENTER)
b12 = generuj_button_cf(f1, "The Work", f3, 0.1, 0.3, CENTER)
b13 = generuj_button_cf(f1, "Contemplation", f4, 0.1, 0.4, CENTER)
b14 = generuj_button_cf(f1, "Quotes", f5, 0.1, 0.5, CENTER)
b1q = generuj_button_q(f1, "Exit", 0.95, 0.95, CENTER)
# f1

###
###
###


n2 = generuj_gnapis(f2, "Free writing.")
t2 = generuj_text(f2, 40, 100, 0.5, 0.5, CENTER,
                  datetime.now().strftime('%H:%M:%S %d-%m-%Y') + "\n\n")
b2 = generuj_button_cf(f2, "Main page", f1, 0.95, 0.95, CENTER)
b2s = generuj_button_s(f2, "Save", t2, 0.9, 0.95, CENTER)
# f2

###
###
###


n3 = generuj_gnapis(f3, "The Work.")

n31 = generuj_napis(f3, "Statement.", 0.1, 0.2, SW)
n32 = generuj_napis(f3, "Is it true?", 0.1, 0.35, SW)
n33 = generuj_napis(
    f3, "Can you absolutely know that it is true?", 0.1, 0.43, SW)
n34 = generuj_napis(f3, "How do you react, what happens, \
when you believe that thought?", 0.1, 0.51, SW)
n35 = generuj_napis(
    f3, "Who would you be without that thought?", 0.1, 0.76, SW)
n36 = generuj_napis(f3, "Turnaround.", 0.6, 0.2, SW)

t31 = generuj_text(f3, 6, 70, 0.1, 0.2, NW, ">")
t32 = generuj_text(f3, 1, 10, 0.1, 0.35, NW, ">")
t33 = generuj_text(f3, 1, 10, 0.1, 0.43, NW, ">")
t34 = generuj_text(f3, 10, 70, 0.1, 0.51, NW, ">")
t35 = generuj_text(f3, 11, 70, 0.1, 0.76, NW, ">")
t36 = generuj_text(f3, 41, 50, 0.6, 0.2, NW, ">")

b3s = generuj_button_s_a(f3, "Save", t31, t32, t33,
                         t34, t35, t36, 0.9, 0.95, CENTER)
b3m = generuj_button_cf(f3, "Main page", f1, 0.95, 0.95, CENTER)
# f3

###
###
###


n4 = generuj_gnapis(f4, "Contemplation.")
b4m = generuj_button_cf(f4, "Main page", f1, 0.95, 0.95, CENTER)
Lista_c = lista_c()


def wylistuj_c():
    pos = 0.2
    a = 0
    for y in Lista_c:
        y = generuj_strone()
        generuj_gnapis(y, Lista_c[a])
        tx = generuj_text(y, 40, 100, 0.5, 0.5, CENTER,
                          datetime.now().strftime('%H:%M:%S %d-%m-%Y')
                          + "\n\n")
        generuj_button_cf(
            y, "Back", f4, 0.95, 0.95, CENTER)
        generuj_button_s(y, "Save", tx, 0.9, 0.95, CENTER)
        generuj_button_cf(f4, Lista_c[a], y, 0.1, pos, CENTER)
        pos += 0.04
        a += 1


wylistuj_c()
# f4

###
###
###


n5 = generuj_gnapis(f5, "Quotes.")
b4m = generuj_button_cf(f5, "Main page", f1, 0.95, 0.95, CENTER)
Lista_q = lista_q()


def wylistuj_q():
    pos = 0.2
    a = 0
    for y in Lista_q:
        y = generuj_strone()
        generuj_gnapis(y, Lista_q[a])
        tx = generuj_text(y, 40, 100, 0.5, 0.5, CENTER,
                          datetime.now().strftime('%H:%M:%S %d-%m-%Y')
                          + "\n\n")
        generuj_button_cf(
            y, "Back", f5, 0.95, 0.95, CENTER)
        generuj_button_s(y, "Save", tx, 0.9, 0.95, CENTER)
        generuj_button_cf(f5, Lista_q[a], y, 0.1, pos, CENTER)
        pos += 0.04
        a += 1


wylistuj_q()
# f5


raise_frame(f1)
root.mainloop()
