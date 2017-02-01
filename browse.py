### Author - Raghav Maheshwari ###

import webbrowser, google


def open_link(address):
    webbrowser.open(address)
    return "there you go"


def get_address(text):
    text = text.split()

    try:
        text = ' '.join(text[text.index('browse') + 1:])
    except ValueError:
        text = ' '.join(text[text.index('open') + 1:])

    open_link(google.lucky(text))

 #get_address('browse fb')



