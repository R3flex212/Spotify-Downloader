import youtube_dl
import shutil
import os
import time
import colorama
from colorama import Fore
from colorama import Style
from index import run, bass_line_freq


#variables
colorama.init()
song_dir = "songs"
attenuate_db = 0
accentuate_db = 0
current_path=(f"D:/Python/Projects/Spotify_Song_Downlaoder/")
dest_path ="D:/Python/Projects/Spotify_Song_Downlaoder/songs/"
spotfy_dir = "/Downloads"
items = list(range(0,10))
l = len(items)


spotify_sign1 = "                      __  .__  _____        ________                       .__                   .___           "
spotify_sign2 ="  ___________   _____/  |_|__|/ ____\__.__. \______ \   ____   ______  _  _|  |   _________    __| _/___________"
spotify_sign3 =" /  ___|____ \ /  _ \   __\  \   __<   |  |  |    |  \ /  _ \ /    \ \/ \/ /  |  /  _ \__  \  / __ |/ __ \_  __ \ "
spotify_sign4 =" \___ \|  |_> >  <_> )  | |  ||  |  \___  |  |    `   (  <_> )   |  \     /|  |_(  <_> ) __ \/ /_/ \  ___/|  | \/ "
spotify_sign5 ="/____  >   __/ \____/|__| |__||__|  / ____| /_______  /\____/|___|  /\/\_/ |____/\____(____  |____ |\___  >__|   "
spotify_sign6 ="     \/|__|                         \/              \/            \/                       \/     \/    \/       "






def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


#song downloader
def download_song():

    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )

    filename = f"{video_title}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
        'newline':True,
        'console-title':True,


    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    time.sleep(3)
    shutil.move(current_path+filename,dest_path)

def return_song_name():
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    return f"{video_info['title']}.mp3"




#main script
if __name__ == '__main__':
    print(Fore.RED + spotify_sign1)
    print(spotify_sign2)
    print(spotify_sign3)
    print(spotify_sign4)
    print(spotify_sign5)
    print(spotify_sign6 + Style.RESET_ALL + "\n")
    time.sleep(2)
    video_url = input("URL:")
    videoinfo = return_song_name()
    print(Fore.GREEN + f"Video selected:   {videoinfo}" + Style.RESET_ALL)
    video_title = input("Title:")
    boost = input("Bass Boost(Y/N):")
    printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
    for i, item in enumerate(items):
        # do stuff
        time.sleep(0.1)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix='Progress:', suffix='Complete', length=50)
    print("\n")
    download_song()
    if boost.lower() == "y":
        #todo make a choice boost lvl adn upload it to github
        accentuate_db = 15
        attenuate_db = 0
        run(accentuate_db,attenuate_db)
        time.sleep(3)
        if os.path.exists(f"songs/{video_title}.mp3"):
            os.remove(f"songs/{video_title}.mp3")
        print(Fore.RED + f"Download complete... >> {video_title}.mp3 >> {spotfy_dir}" + Style.RESET_ALL)
    else:
        accentuate_db = 0
        attenuate_db = 10
        run(accentuate_db, attenuate_db)
        time.sleep(3)
        if os.path.exists(f"songs/{video_title}.mp3"):
            os.remove(f"songs/{video_title}.mp3")
        print(Fore.RED + f"Download complete... >> {video_title}.mp3 >> {spotfy_dir}" + Style.RESET_ALL)




