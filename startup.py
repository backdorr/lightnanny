#!/usr/bin/python

import smtplib
import socket
import os
import sys

g_settings = [ \
   'gmail_user="your_gmail_user"\n', \
   'gmail_pass="your_gmail_pass"\n', \
   'notification_recipients=["notification_recipient"]\n', \
   ] 

config = {}
if os.path.isfile("startup.cfg"):
   execfile("startup.cfg", config)
else:
   print "startup.cfg doesn't exist"
   file = open("startup.cfg","w")
   for item in g_settings:
      file.write(item) 
   print "created startup.cfg, please add your details"
   sys.exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))
ipaddress = s.getsockname()[0]

sender = config["gmail_user"]
password = config["gmail_pass"]
receivers = config["notification_recipients"]

message = """From: 
To: Light Nanny Recipients
Subject: Light Nanny Startup

The Light Nanny has been rebooted and has the local ip address of %s
""" % ipaddress

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
   smtpObj.ehlo()
   smtpObj.starttls()
   smtpObj.ehlo()
   smtpObj.login(sender, password)
   smtpObj.sendmail(sender, receivers, message)
   smtpObj.close()
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"
