from datetime import datetime
import pygame
import time


def saat():
    hour = int(input("Saati Giriniz: "))
    if ((hour >= 0) and (hour < 24)):
        return hour
    else:
        print("Saat Aralığının Dışında Değer Girdiniz, Lütfen 0-24 Arası Değer Giriniz")
        return saat()


def dakika():
    minute = int(input("Dakikayı Giriniz: "))
    if ((minute >= 0) and (minute < 60)):
        return minute
    else:
        print("Dakika Aralığının Dışında Değer Girdiniz, Lütfen 0-60 Arası Değer Giriniz")
        return dakika()


def saniye():
    second = int(input("Saniyeyi Giriniz: "))
    if ((second >= 0) and (second < 60)):
        return second
    else:
        print("Saniye Aralığının Dışında Değer Girdiniz, Lütfen 0-60 Arası Değer Giriniz")
        return saniye()


def tekrar():
    x = int(input("Alarm Tekrar Miktarını Giriniz: "))
    if (x < 0):
        print("0'dan Büyük Bir Sayı Giriniz")
        return tekrar()
    else:
        return x

i = 0
a = saat()
b = dakika()
c = saniye()
d = tekrar()

while True:

    now = datetime.now()
    dt = datetime.strftime(now, '%H:%M:%S')
    print(dt)
    time.sleep(1)

    if (dt == f"{a}:{b}:{c}"):
        while i < d:
            pygame.init()
            pygame.mixer.music.load("alarm.mp3")
            pygame.mixer.music.play()
            print("ALARM!")
            while pygame.mixer.music.get_busy():
                pygame.event.get()
            i += 1
    break
