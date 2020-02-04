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

frame1 = Frame(root, background='black',)

frame2 = Frame(root, background='black',)

frame3 = Frame(root, background='black',)

frame4 = Frame(root, background='black',)
# FRAMY

for frame in (frame1, frame2, frame3, frame4):
    # frame.place(x=0, y=0, relwidth=1, relheight=1)
    frame.grid(row=0, column=0, sticky='news')
# ulozyni framow


###
###
###


Napis1 = Label(frame1, text="Welcome to the Journal!",
               font=("arial", 30, "bold"), fg='white', bg='black')
Napis1.place(relx=0.5, rely=0.1, anchor=CENTER)

Button11 = Button(frame1, text="Free writing",
                  command=lambda: raise_frame(frame2))
Button11.place(relx=0.1, rely=0.2, anchor=CENTER, )

Button12 = Button(frame1, text="The Work",
                  command=lambda: raise_frame(frame3))
Button12.place(relx=0.1, rely=0.3, anchor=CENTER, )

Button13 = Button(frame1, text="Contemplation",
                  command=lambda: raise_frame(frame4))
Button13.place(relx=0.1, rely=0.4, anchor=CENTER, )

Button1quit = Button(frame1, text="Exit", command=lambda: quit())
Button1quit.place(relx=0.95, rely=0.95, anchor=CENTER)


###
###
###


Napis2 = Label(frame2, text="Free writing.",
               font=("arial", 30, "bold"), fg='white', bg='black')
Napis2.place(relx=0.5, rely=0.1, anchor=CENTER)

Text2 = Text(frame2, height=40, width=100, setgrid=True)
Text2.place(relx=0.5, rely=0.5, anchor=CENTER)   # centers it
Text2.insert(END, datetime.now().strftime('%H:%M:%S %d-%m-%Y') + "\n\n")

Button2 = Button(frame2, text="Main page", command=lambda: raise_frame(frame1))
Button2.place(relx=0.95, rely=0.95, anchor=CENTER)

Button2save = Button(frame2, text='Save', command=lambda: saveFile(Text2))
Button2save.place(relx=0.90, rely=0.95, anchor=CENTER, )


###
###
###


Napis3 = Label(frame3, text="The Work",
               font=("arial", 30, "bold"), fg='white', bg='black')
Napis3.place(relx=0.5, rely=0.1, anchor=CENTER)

Napis31 = Label(frame3, text="Statement", fg='white', bg='black')
Napis31.place(relx=0.1, rely=0.2, anchor=SW)

Text31 = Text(frame3, height=6, width=70)
Text31.place(relx=0.1, rely=0.2, anchor=NW)
Text31.insert(END, ">")

Napis32 = Label(frame3, text="Is it true?", fg='white', bg='black')
Napis32.place(relx=0.1, rely=0.35, anchor=SW)

Text32 = Text(frame3, height=1, width=10)
Text32.place(relx=0.1, rely=0.35, anchor=NW)
Text32.insert(END, ">")

Napis33 = Label(frame3, text="Can you absolutely know that it is true?",
                fg='white', bg='black')
Napis33.place(relx=0.1, rely=0.43, anchor=SW)

Text33 = Text(frame3, height=1, width=10)
Text33.place(relx=0.1, rely=0.43, anchor=NW)
Text33.insert(END, ">")

Napis34 = Label(frame3, text="How do you react, what happens, \
when you believe that thought?",
                fg='white', bg='black')
Napis34.place(relx=0.1, rely=0.51, anchor=SW)

Text34 = Text(frame3, height=10, width=70)
Text34.place(relx=0.1, rely=0.51, anchor=NW)
Text34.insert(END, ">")

Napis35 = Label(frame3, text="Who would you be without that thought?",
                fg='white', bg='black')
Napis35.place(relx=0.1, rely=0.76, anchor=SW)

Text35 = Text(frame3, height=11, width=70)
Text35.place(relx=0.1, rely=0.76, anchor=NW)
Text35.insert(END, ">")

Napis36 = Label(frame3, text="Turnaround", fg='white', bg='black')
Napis36.place(relx=0.6, rely=0.2, anchor=SW)

Text36 = Text(frame3, height=41, width=50)
Text36.place(relx=0.6, rely=0.2, anchor=NW)
Text36.insert(END, ">")

Button2save = Button(frame3, text='Save',
                     command=lambda: combine(Text31, Text32, Text33, Text34,
                                             Text35, Text36))
Button2save.place(relx=0.90, rely=0.95, anchor=CENTER, )

Button3 = Button(frame3, text="Main page", command=lambda: raise_frame(frame1))
Button3.place(relx=0.95, rely=0.95, anchor=CENTER)


###
###
###

Napis4 = Label(frame4, text="Contemplation",
               font=("arial", 30, "bold"), fg='white', bg='black')
Napis4.place(relx=0.5, rely=0.1, anchor=CENTER)

Lista1 = ['Who am I?', 'What is death?', 'What is this?']


def wylistuj():
    pos = 0.2
    for x in Lista1:
        nap = Label(frame4, text=x)
        nap.place(relx=0.1, rely=pos, anchor=CENTER)
        pos += 0.03


wylistuj()

Button4 = Button(frame4, text="Main page", command=lambda: raise_frame(frame1))
Button4.place(relx=0.95, rely=0.95, anchor=CENTER)


raise_frame(frame1)
root.mainloop()
