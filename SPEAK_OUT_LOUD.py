### Author - Raghav Maheshwari ###

import pyperclip
from AudioIO import speak

f = open(pyperclip.paste(), 'r')
text = f.readlines()

for i in text:
    print(i)
    speak(i)