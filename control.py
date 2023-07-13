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


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(22, GP+-IO.IN)
yel= LED(22)


subject='Uyarı: Kedin Hareket Etti!!'
SMTP_SERVER='smtp.gmail.com'
SMTP_PORT=587
USERNAME=''
PASSWORD=''
RECIEVER_EMAIL=''

filename_part1="kedimhepyanimda"
file_ext=".mp4"
now = datetime.now()
current_datetime = now.strftime("%d-%m-%Y_%H:%M:%S")
filename=filename_part1+"_"+current_datetime+file_ext
filepath="/home/pi/python_code/"


def istemci():
 with open('login.txt', 'r') as file:
  lines = file.readlines()
  username = lines[0].strip()
  password = lines[1].strip()
  receiver_email = lines[2].strip()
 return username, password, receiver_email


def islem_günlügü(message):
 with open('log.txt', 'a') as file:
  now = datetime.now()
  timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
  log_entry = f"[{timestamp}] {message}"
  file.write(log_entry + '\n')


def hata_kontrol(error_message):
 islem_günlügü(f"ERROR: {error_message}")
 print(f"ERROR: {error_message}")
