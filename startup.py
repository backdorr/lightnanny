#!/usr/bin/python

config = {}
execfile("startup.cfg", config)

import smtplib
import socket
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
