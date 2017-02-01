### Author - Raghav Maheshwari ###

import requests, bs4, AudioIO
from os import chdir
from settings import MP3_DIR


def download_song(link, name):
    chdir(MP3_DIR)
    AudioIO.speak('Downloading ' + name + '...')
    res = requests.get(link)
    try:
        res.raise_for_status()
    except:
        AudioIO.speak('Downloading Error')
        return False
    song = open(name, 'wb')
    for chunk in res.iter_content(100000):
        song.write(chunk)
    song.close()
    AudioIO.speak('Download finished')
    return True


def download_link(addr):
    res = requests.get(addr)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    s = soup.select('a')
    link = []
    for i in s:
        try:
            if "Download In" in i.get_text('strong'):# and "Quality" in i.get_text('strong'):
                link.append(i.get('href'))
        except:
            pass
    try:
        name = link[-1][len(link[-1]) - link[-1][::-1].find('/'):]
    except IndexError:
        return False
    return download_song(link[-1], name)


def page_link(name):
    name += ' mp3mad'
    res = requests.get('https://google.com/search?q=' + name)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    opt = soup.select('.r a')
    for link in opt[:3]:
        try:
            addr = link.get('href')
            addr = addr[7:addr.index('&')]
            print('trying -> ' + addr)
            if download_link(addr):
                break
        except IndexError:
            pass
    else:
        return "No Link found"



#page_link(input())

