#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from AudioIO import listen, speak
from MainEngine import main
from settings import LOGO_PATH
from _thread import start_new_thread


def getTextInput():
    main(box.get() + user_command.get())


def getVoInput():
    box.set('')
    user_command.delete(0, END)
    speak('listening')
    text = listen().lower()
    user_command.insert(0, text)
    start_new_thread(main, (text,))


def open_log():
    main('open file microphone_log')


def open_req():
    main('open file requirements')


root = Tk()
frame = Frame(root, height=200, width=20)
root.title('Nancy')

# Menubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Logs", command=open_log)
filemenu.add_command(label="Requirements", command=open_req)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Extras", menu=filemenu)

root.config(menu=menubar)

# Label - Logo
photo = PhotoImage(file=LOGO_PATH)
Label(root, image=photo).grid(row=0, columnspan=2)

# ComboBox - Select Command
value = StringVar()
box = ttk.Combobox(root, textvariable=value, state='readonly')
box['values'] = ('google ', 'play audio ', 'play video ', 'download audio ', 'download video ',
                 'open file ', 'open folder ', 'open drive ', 'execute ', 'browse ')
box.set("Select Command")
box.grid(row=1, column=0)


# Entry - User Request
user_command = Entry(root, bd=2)
user_command.grid(row=1, column=1)

# Button - Search
btn_search = Button(root, text="Search", width=18, command=getTextInput,
                    bg="#4169e1", fg="white").grid(row=2, column=1)

# Button - Microphone
btn_voInput = Button(root, text="Microphone", width=19, command=getVoInput,
                     bg="#DF0101", fg="white").grid(row=2, column=0)


root.mainloop()

