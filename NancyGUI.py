### Author - Raghav Maheshwari ###

#!/usr/bin/python3
from tkinter import *
from AudioIO import listen, speak
from MainEngine import main


def getTextInput():
    main(user_command.get())


def getVoInput():
    user_command.delete(0, END)
    speak('listening')
    text = listen().lower()
    user_command.insert(0, text)
    main(text)


root = Tk()
frame = Frame(root, height=200, width=200)

#action = Menubutton(root, text="Action")
#action.grid()
#options = Menu(action, tearoff=0)
#action["options"] = options


Label(root, text="Command").grid(row=0, column=0)
user_command = Entry(root, bd=1)
user_command.grid(row=0, column=2)

#photo = PhotoImage(file="microphone.png")
btn_search = Button(root, text="Search", width=10, command=getTextInput).grid(row=1, column=0)
btn_voInput = Button(root, text="Microphone", width=10, command=getVoInput).grid(row=1, column=1)


root.mainloop()

