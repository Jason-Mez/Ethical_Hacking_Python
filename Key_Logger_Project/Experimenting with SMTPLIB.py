#!/usr/bin/env python3

import smtplib
def send_mail(email, password, message):
    #Creating an instance of an SMTP server.
    #this will be used to send an emai.
    server = smtplib.SMTP("smtp.gmail.com", 587)
    #This will start the connection.
    server.starttls()
    #Loggin in to the server.
    server.login(email, password)
    #Sending the e-mail.
    server.sendmail(email, email, message)
    #Quitting or server with the server.
    server.quit() 

send_mail("testingj314@gmail.com", "admin123admin", "This was used with Python. ")
