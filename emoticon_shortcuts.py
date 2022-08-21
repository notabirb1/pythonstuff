# Requires global_hotkeys, pywin32, and keyboard modules.
# https://stackoverflow.com/questions/67505554/python-keyboard-module-add-hotkey-is-not-working-after-you-lock-windows-once-he
from global_hotkeys import *
import keyboard

import time

runScript = True

# Define what each keybind should do
def input_shrug():
    keyboard.write("¯\_(ツ)_/¯")

def input_invisible_unicode_character():
    keyboard.write("⠀")

def input_bear():
    keyboard.write("ʕ •ᴥ•ʔ")

def input_tableflip():
    keyboard.write("(╯°□°）╯︵ ┻━┻")

def input_disapprove():
    keyboard.write("ಠ_ಠ")


# Declare keybinds
bindings = [
    [["control", "alt", "1"], None, input_shrug], # ¯\_(ツ)_/¯
    [["control", "alt", "2"], None, input_invisible_unicode_character], # Invisible Unicode Character (⠀)
    [["control", "alt", "3"], None, input_bear], # ʕ •ᴥ•ʔ
    [["control", "alt", "4"], None, input_tableflip], # (╯°□°）╯︵ ┻━┻)
    [["control", "alt", "5"], None, input_disapprove], # ಠ_ಠ
]

# Register Keybinds
register_hotkeys(bindings)

# Listen for keypresses
start_checking_hotkeys()

# Keep the script running at 0% CPU Usage
while runScript:
    time.sleep(0.1)