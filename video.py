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
from control import hata_kontrol


def video_cek():
    try:
        camera.start_preview()
        camera.start_recording('/home/pi/python_code/kedimhepyanimda.h264')
        camera.wait_recording(10)
        camera.stop_recording()
        camera.stop_preview()
    except Exception as e:
        hata_kontrol(f"Video kaydedilirken bir hata oluştu: {str(e)}")


def dosya_sil():
    try:
        if os.path.exists("/home/pi/python_code/newvideo.h264"):
            os.remove("/home/pi/python_code/newvideo.h264")
        if os.path.exists(filepath + filename):
            os.remove(filepath + filename)
    except Exception as e:
        hata_kontrol(f"Dosya silinirken bir hata oluştu: {str(e)}")

    if os.path.exists(filepath + filename):
        os.remove(filepath + filename)
    else:
        print("Dosya Silindi")


camera = PiCamera()