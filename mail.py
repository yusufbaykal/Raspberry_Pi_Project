import smtplib, email, os
from gpiozero import LED
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

from picamera import PiCamera
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

from control import islem_günlügü
from control import hata_kontrol


def mail_gönder():
 try:
  message = MIMEMultipart()
  message["From"] = USERNAME
  message["To"] = RECEIVER_EMAIL
  message["Subject"] = subject

  message.attach(MIMEText('plain'))
  attachment = open(filepath + filename, "rb")

  mime_base = MIMEBase('application', 'octet-stream')
  mime_base.set_payload((attachment).read())

  encoders.encode_base64(mime_base)
  mime_base.add_header('Content-Disposition', "attachment; filename= " + filename)

  message.attach(mime_base)
  text = message.as_string()

  session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
  session.ehlo()
  session.starttls()
  session.ehlo()

  session.login(USERNAME, PASSWORD)
  session.sendmail(USERNAME, RECEIVER_EMAIL, text)
  session.quit()
  islem_günlügü("Email Gönderildi")
 except Exception as e:
  hata_kontrol(f"Email gönderilirken bir hata oluştu: {str(e)}")