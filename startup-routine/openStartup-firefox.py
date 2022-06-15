# Firefox Only
# To work properly, this script requires that you set "browser.sessionstore.restore_pinned_tabs_on_demand" in about:config to true.
# You also need the extension "Toggle Pin Tab"
# Don't interact with the programs until they all open

import pyautogui
import os
import time

# Commands for specific tabs
#spotifyCommand = r'C:\"Program Files\Mozilla Firefox\firefox.exe" -new-window https://open.spotify.com'
youtubeCommand = r'C:\"Program Files\Mozilla Firefox\firefox.exe" -new-tab https://youtube.com'
rodentCommandLinux = r'C:\"Program Files\Mozilla Firefox\firefox.exe" -new-tab https://reddit.com/r/Linux'
rodentCommandMinecraft = r'C:\"Program Files\Mozilla Firefox\firefox.exe" -new-tab https://reddit.com/r/Minecraft'
gmailCommand = r'C:\"Program Files\Mozilla Firefox\firefox.exe" -new-tab https://mail.google.com'

discordCommand = r'C:\"Program Files\Mozilla Firefox\firefox.exe" -new-window https://discord.com/channels/@me'

# Spotify opening sequence
# Disabled due to Firefox opening pinned tabs by default, making this unecessary.

#os.system(spotifyCommand) # Open Spotify
#time.sleep(3) # Wait
#pyautogui.hotkey('alt', 'p') # Pin Spotify
#time.sleep(1) # Give it time to pin

# Everything else opening sequence
os.system(youtubeCommand) # Open YouTube
os.system(rodentCommandLinux) # Open r/Linux
os.system(rodentCommandMinecraft) # Open r/Minecraft

# Discord Opening Sequence
os.system(discordCommand) # Open Discord in a new window
time.sleep(1) # Wait
pyautogui.hotkey('winleft', 'shift', 'right') # Move to second monitor
time.sleep(7) # Wait
pyautogui.hotkey('ctrl', 'shift', 'm') # Unmute microphone

# Gmail Opening Sequence
os.system(gmailCommand) # Open Gmail
pyautogui.hotkey('ctrl', 'tab') # Return Window Focus to Discord