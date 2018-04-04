#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: kini
@contect: https://github.com/dongjunjie/simple_mailer
"""
import os
import ConfigParser
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

# load config
cfg = ConfigParser.ConfigParser()
current_path = os.path.split(os.path.realpath(__file__))[0]
cfg.read(current_path + "/mail.conf")
HOST_SERVER = cfg.get("server","host")
USER = cfg.get("sender","user")
PWD = cfg.get("sender","pwd")
SENDER = cfg.get("sender","mail")
RECEIVER = cfg.get("receiver","mail")
TITLE = cfg.get("mail","title")
CONTENT = cfg.get("mail","content")
    
# begin login
smtp = SMTP_SSL(HOST_SERVER)
smtp.set_debuglevel(1)
smtp.ehlo(HOST_SERVER)
smtp.login(USER, PWD)

# generate content
msg = MIMEText(CONTENT, "plain", 'utf-8')
msg["Subject"] = Header(TITLE, 'utf-8')
msg["From"] = SENDER
msg["To"] = RECEIVER
smtp.sendmail(SENDER, RECEIVER, msg.as_string())
smtp.quit()
    

