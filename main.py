import smtplib
import email
import os
from gpiozero import LED
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from picamera import PiCamera
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
from control import istemci
from control import islem_günlügü
from control import hata_kontrol
from video import video_cek
from mail import mail_gönder
from video import dosya_sil



def kontrol():
    while True:
        i = GPIO.input(11)
        if i == 1:
            yel.on()
            islem_günlügü("Hareket Algılandı")
            video_cek()
            sleep(2)
            yel.off()
            res = os.system("MP4Box -add /home/pi/python_code/kedimhepyanimda.h264 /home/pi/python_code/kedimhepyanimda.mp4")
            os.system("mv /home/pi/python_code/kedimhepyanimda.mp4 " + filepath + filename)
            mail_gönder()
            sleep(2)
            dosya_sil()

if __name__ == "__main__":
    USERNAME, PASSWORD, RECEIVER_EMAIL = istemci()
    kontrol()