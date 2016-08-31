#!/usr/bin/env python
import time
import fcntl
import os
import signal

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
import smtplib
import os
import glob
import subprocess

FNAME = "/home/elgin/"

#subject: project data update.


#path: 
#Data upload completed for the above project.
#File name:
#File size:


def handler(signum, frame):    
    result = "Project Data Uploaded in path: %s " % (FNAME,)
    if result:
        #list = os.listdir(FNAME)
        #pairs = []
        #for file in list:    
            #location = os.path.join(FNAME, file)    
            #size = os.path.getsize(location)
            #pairs.append((size, file))
        #pairs.sort(key=lambda s: s[0]) 
        #for pair in pairs:
            #print(pair)    
        
        fromaddr = "lrbattendance@gmail.com"
        toaddr = "admin@leucinerichbio.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Project Data Files Upload"
        body = "Data Upload completed for the above project. path: %s " % (FNAME,)
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("lrbattendance@gmail.com", "lrbctog#1")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)

signal.signal(signal.SIGIO, handler)
fd = os.open(FNAME,  os.O_RDONLY)
fcntl.fcntl(fd, fcntl.F_SETSIG, 0)
fcntl.fcntl(fd, fcntl.F_NOTIFY,
            fcntl.DN_MODIFY | fcntl.DN_CREATE | fcntl.DN_MULTISHOT)

while True:
    time.sleep(1000000)


            
