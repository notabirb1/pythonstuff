import ctypes
import requests
from datetime import date
import time

datehyphenint = date.today() # Gets the date, with hyphens, those need to be removed
datehyphen = str(datehyphenint)
date = datehyphen.replace('-', '') # Removes the hyphens and stores it as 'date'

image_url_part_1 = "https://bingwallpaperimages.azureedge.net/hpimages/Latest/3840x2160/" # First half of the url for the image of the day
image_url_part_2 = ".jpg" # Second part
image_url = image_url_part_1 + date + image_url_part_2 # Adds the date into the middle of the two parts to create the full link, this is necessary due to how the Bing image of the day urls work

r = requests.get(image_url)

with open("wallpaperimage.jpg",'wb') as f: # Stores the image as wallpaperimage.png
    f.write(r.content)
    
time.sleep(5)
SPI_SETDESKTOPWALLPAPER=20
wallpaperpath = "C:/YOURDIRECTORY/wallpaperimage.jpg" # The path to the wallpaper (change this if you use it)
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0, wallpaperpath, 0) # Sets the wallpaper