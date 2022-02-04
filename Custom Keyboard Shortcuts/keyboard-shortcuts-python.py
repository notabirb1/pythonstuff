import subprocess
import keyboard
import time

runScript = True

while runScript: # Main Loop
    
    time.sleep(0.01)
    openTerminal = False
    openCalculator = False
    if keyboard.is_pressed('ctrl+alt+t'):
        openTerminal = True
    if keyboard.is_pressed('ctrl+alt+c'):
        openCalculator = True
    while openTerminal:
        subprocess.call(["wt"])
        time.sleep(1)
        openTerminal = False
    while openCalculator:
        subprocess.call(["calc"])
        time.sleep(1)
        openCalculator = False
    time.sleep(0.01)