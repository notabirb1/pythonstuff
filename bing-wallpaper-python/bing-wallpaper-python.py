# A script to change the wallpaper to the Bing Image Of The Day, without relying on the official program.
# Windows Only
# It is recommended to run this script at around 8:00 - 10:00 A.M. EDT
import requests
from datetime import datetime, date
import time
import os
import ctypes

# Get Current Time (https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time)
now = datetime.now()

current_time_original = now.strftime("%H:%M:%S")
current_time = current_time_original.replace(':', '')

# Variables
minimumtime = "080000"
workingDirectory = os.getcwd()
datehyphenint = date.today()
datehyphen = str(datehyphenint)
date = datehyphen.replace('-', '')
pathToImg = workingDirectory + "\wallpaperimage.jpg"

# Download and store image
image_url_part_1 = "https://bingwallpaperimages.azureedge.net/hpimages/Latest/3840x2160/"
image_url_part_2 = ".jpg"
image_url = image_url_part_1 + date + image_url_part_2

if minimumtime < current_time: # Check if the time is >8:00 A.M.
    r = requests.get(image_url)
    with open("wallpaperimage.jpg",'wb') as f:
        f.write(r.content)

    # Set Wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, pathToImg, 3)