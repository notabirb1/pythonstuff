# Ungoogled Chromium + YT Music Adaptation
# Don't interact with the programs until they all open

import pyautogui
import os
import time

# Commands for specific tabs
youtubeCommand = 'start "" "https://youtube.com"'
rodentCommandLinux = 'start "" "https://reddit.com/r/Linux"'
rodentCommandMinecraft = 'start "" "https://reddit.com/r/Minecraft"'
gmailCommand = 'start "" "https://mail.google.com"'

discordCommand = r'C:\"Users\notabirb1\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord.lnk"'

# Everything else opening sequence
os.system(youtubeCommand) # Open YouTube
time.sleep(0.5)
os.system(rodentCommandLinux) # Open r/Linux
time.sleep(0.5)
os.system(rodentCommandMinecraft) # Open r/Minecraft

# Discord Opening Sequence
os.system(discordCommand) # Open Discord in a new window
#time.sleep(1) # Wait
#pyautogui.hotkey('winleft', 'shift', 'right') # Move to second monitor
time.sleep(7) # Wait
pyautogui.hotkey('ctrl', 'shift', 'm') # Unmute microphone

# Gmail Opening Sequence
#os.system(gmailCommand) # Open Gmail
#pyautogui.hotkey('ctrl', 'tab') # Return Window Focus to Discord