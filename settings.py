### Author - Raghav Maheshwari ###

from wolframalpha import Client
from os import listdir

app_id = "KHHH6P-HTUJE286QJ"
client = Client(app_id)

LOGO_PATH  = '/home/imnobody0396/Documents/Nancy-The-Virtual-Assistant/logo.png'
             #'/home/imnobody0396/Desktop/nancy.png')
HOME_DIR   = '/home/imnobody0396/'
DRIVE_DIR  = '/media/imnobody0396/'
LOG_DIR    = '/home/imnobody0396/Documents/Nancy-The-Virtual-Assistant/'
LYRICS_DIR = '/media/imnobody0396/Green/Videos/Lyrics/'
MP3_DIR    = '/media/imnobody0396/Green/Music/'
MP4_DIR    = '/media/imnobody0396/Green/Videos/'
IGNORE_DIRS= ['/media/imnobody0396/Green/Matlab', '/media/imnobody0396/Blue/.Tempp']

DRIVES = [dir for dir in listdir(DRIVE_DIR)]