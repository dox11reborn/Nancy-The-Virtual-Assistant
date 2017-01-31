import webbrowser, google


def open_link(address):
    webbrowser.open(address)
    return "there you go"


def get_result(text):
    text = text.split()
    text = ' '.join(text[text.index('google') + 1:])
    #print(google.lucky(text))
    open_link(google.lucky(text))

#get_result('google India')