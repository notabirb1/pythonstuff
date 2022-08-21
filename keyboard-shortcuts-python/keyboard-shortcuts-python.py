# Requires global_hotkeys, pywin32, and keyboard modules.
# A script for adding custom keyboard shortcuts to Windows.

# https://stackoverflow.com/questions/67505554/python-keyboard-module-add-hotkey-is-not-working-after-you-lock-windows-once-he
from global_hotkeys import *
import keyboard
import subprocess
import time

runScript = True

# Define what each keybind should do
def openTerminal():
    subprocess.call(["wt"])

def openCalculator():
    subprocess.call(["calc"])

# Keybinds
bindings = [
    [["control", "alt", "t"], None, openTerminal], # Terminal
    [["control", "alt", "c"], None, openCalculator], # Calculator
]

# Register keybinds
register_hotkeys(bindings)

# Listen for keypresses
start_checking_hotkeys()

# Keep the script running
while runScript:
    time.sleep(0.1)