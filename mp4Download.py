### Author - Raghav Maheshwari ###

import AudioIO
from os import chdir
from pytube import YouTube
from pprint import pprint
from google import lucky
from settings import MP4_DIR


def vid_download(link):
    try:
        chdir(MP4_DIR)
    except:
        return 'Download path is not mounted.'
    try:
        yt = YouTube(link)
    except:
        print("Cipher Error")

    pprint(yt.get_videos())
    quality = ['720p', '480p', '360p']
    for i in quality:
        try:
            video = yt.get('mp4', i)
            AudioIO.speak('Downloading in ' + i + " " + yt.filename)
            video.download('.')
            AudioIO.speak('Download Complete')
            break
        except:
            continue
    else:
        return 'Not found in good quality'


def youtube_link(text):
    #res = requests.get('https://www.google.com/search?q=' + text)
    #res.raise_for_status()
    #soup = bs4.BeautifulSoup(res.text, 'lxml')
    #link = soup.select_one('cite').getText()
    #print(text,link, lucky(text))
    try:
        vid_download(lucky(text))
    except Exception as ex:
        AudioIO.speak("Age Restricted Video")

#youtube_link(input() + ' youtube')
#vid_download('https://www.youtube.com/watch?v=Ib8XaRKCAfo')
