import os
from pytube import YouTube

os.system("clear")
print("__    __  _____        _     _   _   _____   _____   _____       ")
print("\ \  / / |_   _|      | |   / / | | |  _  \ | ____| /  _  \      ")
print(" \ \/ /    | |        | |  / /  | | | | | | | |__   | | | |      ")
print("  \  /     | |        | | / /   | | | | | | |  __|  | | | |      ")
print("  / /      | |        | |/ /    | | | |_| | | |___  | |_| |      ")
print(" /_/       |_|        |___/     |_| |_____/ |_____| \_____/      ")
print("                    Abdo sleem (*__^) ")
print("  ")
print("               ==> highest resolution <== ")
print(" ")
url = input("  Video Link ==> ")
my_video = YouTube(url, on_progress_callback=on_progress)
print(" ")
print(" ")
print(" Downloading ...    Please be patient (^__^)")
##my_video.download()
my_video = my_video.streams.get_highest_resolution()
my_video.download(output_path="/sdcard")
print("     ")
print("  ")
print ("  Download Successfully !!!")