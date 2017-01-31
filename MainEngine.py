#!/usr/bin/python3
import notify2, nautilus
import tkinter as tk
from re import match,search
from os import chdir
from settings import LOG_DIR, LOGO_PATH
from datetime import datetime
from temperature import getTemperature
from meaning import getMeaning
from browse import get_address
from search import get_result
from mp3download import page_link
from mp4Download import youtube_link
from lyrics import lyrics_down
from AudioIO import speak


def update_log(text):   # Updating Microphone Log
    chdir(LOG_DIR)
    with open('microphone_log.txt', 'a') as f:
        f.write(str(datetime.utcnow()) + " " + text + '\n')


class StopApp(tk.Tk):   # Pause Nancy code
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Nancy Stopped")
        self.button = tk.Button(self, text="Start Nancy", bg="#09C889", fg="white", command=self.on_button)
        self.button.pack()

    def on_button(self):
        self.destroy()


def nancy_notify(text):     #Desktop Notification
    notify2.init('Nancy')
    n = notify2.Notification('Nancy', text, icon=LOGO_PATH)
    n.show()


def main(text):
    #nancy_notify('Virtual Assistant Started')
    #text = ""
    #while text != "terminate":
    #if text == "":
    #    speak('On your mark sir')
    #else:
    #    speak('ready sir')

    #text = "download video ok jaanu title song"
    #text = listen().lower()
    #text = listen().lower()
    #nancy_notify(text)
    print(text)
    update_log(text)

    if text in ["who are you", "introduce yourself"]:
        speak('I am Nancy, your personal assistant.')
        return
    elif text == "describe yourself":
        speak("I am Nancy, your personal assistant. I use python's speech recognition module "
                          "to understand voice input, and google's text to speech technology to give output.")
        return
    '''
    elif text in ["stop", "go to sleep"]:
        speak('Okay sir')
        stop = StopApp()
        stop.mainloop()
        continue

    elif text == "connection problem":
        nancy_notify('connection problem Nancy exiting...')
        exit()

    elif text in ["didn't get you", "terminate"]:
        if text == "terminate":
            nancy_notify('Virtual Assistant Exited')
            speak("Bye Bye")
        else:
            speak(text)
        #continue
    '''
    #speak('fetching results please wait')

    if match(r'^.*(folder)|(directory) .*$', text):
        speak(nautilus.gen_folder_path(text))

    elif search(r'drive', text):
        speak(nautilus.gen_drive_path(text))

    elif search(r'(meaning)|(define)', text):
        speak(getMeaning(text))

    elif search(r'temperature', text):
        speak(getTemperature(text))

    elif search(r'(run)|(execute)', text):
        speak(nautilus.open_gnome(text))

    elif search(r'(browse)', text):
        speak(get_address(text))

    elif search(r'(google)|(search)', text):
        speak(get_result(text))

    #elif search(r'download\s(audio)|(song)', text):
    #    speak(page_link(' '.join(text.split()[2:])))

    elif search(r'download\s(video)|(mp4)', text):
        speak(youtube_link(' '.join(text.split()[2:])))

    elif search(r'download\s(lyrics)', text):
        speak(lyrics_down(text))

    else:
        speak(nautilus.gen_file_path(text))


#if __name__ == '__main__':
#    main()
