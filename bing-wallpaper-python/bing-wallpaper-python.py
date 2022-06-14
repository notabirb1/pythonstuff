# A script to change the wallpaper to the Bing Image Of The Day, without relying on the official program.
# Windows Only

# This script will only work past a certain point in the day.
# This is due to the Bing Image of The Day being uploaded to their servers at an unknown time.
# It is recommended to run this script at around 8:00 - 10:00 A.M. EDT
import requests
from datetime import date
import time
import os
import ctypes

# Variables
workingDirectory = os.getcwd()
datehyphenint = date.today()
datehyphen = str(datehyphenint)
date = datehyphen.replace('-', '')
pathToImg = workingDirectory + "\wallpaperimage.jpg"

# Download and store image
image_url_part_1 = "https://bingwallpaperimages.azureedge.net/hpimages/Latest/3840x2160/"
image_url_part_2 = ".jpg"
image_url = image_url_part_1 + date + image_url_part_2
r = requests.get(image_url)
with open("wallpaperimage.jpg",'wb') as f:
    f.write(r.content)

# Set Wallpaper
ctypes.windll.user32.SystemParametersInfoW(20, 0, pathToImg, 3)