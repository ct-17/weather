#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import math
from pprint import pprint
apikey = "964208c4456c12982d773d5ba970b270"
units="si"

city = input("Chon thanh pho: ")
location = {"hanoi":[{"latitude":21.0277644},{"longitude":105.83415979999995}],"hochiminh":[{"latitude":10.83333},{"longitude":106.63278}], "haiphong":[{"latitude":20.86194},{"longitude":106.68028}], "cantho":[{"latitude":10.03278},{"longitude":105.78389}], "danang":[{"latitude":16.05194},{"longitude":108.21528}], "bienhoa":[{"latitude":10.95694},{"longitude":106.84306}], "thanhhoa":[{"latitude":19.80750},{"longitude":105.77639}], "nhatrang":[{"latitude":12.23889},{"longitude":109.19694}], "vungtau":[{"latitude":10.34583},{"longitude":107.08472}], "thuduc":[{"latitude":10.88333},{"longitude":106.72694}], "hue":[{"latitude":16.46278},{"longitude":107.58472}], "buonmathuat":[{"latitude":12.66667},{"longitude":108.03889}], "thainguyen":[{"latitude":21.56750},{"longitude":105.82556}], "vinh":[{"latitude":18.68083},{"longitude":105.68167}], "haiphong":[{"latitude":20.93972},{"longitude":106.31250}], "thudaumot":[{"latitude":10.99333},{"longitude":106.65611}], "namdinh":[{"latitude":20.42000},{"longitude":106.16833}], "rachgia":[{"latitude":10.02083},{"longitude":105.09028}], "halong":[{"latitude":20.97194},{"longitude":107.04528}], "minhtho":[{"latitude":10.35417},{"longitude":106.36528}], "quynhon":[{"latitude":13.77500},{"longitude":109.23333}], "thaibinh":[{"latitude":20.44750},{"longitude":106.33750}], "dalat":[{"latitude":11.94556},{"longitude":108.44222}], "phanthiet":[{"latitude":10.92222},{"longitude":108.10944}], "camau":[{"latitude":9.18361},{"longitude":105.15000}], "longthanh":[{"latitude":10.79306},{"longitude":107.01361}], "tuyhoa":[{"latitude":13.08222},{"longitude":109.31611}], "campha":[{"latitude":21.01611},{"longitude":107.33194}], "pleiku":[{"latitude":13.98361},{"longitude":1080.00000}], "soctrang":[{"latitude":9.60389},{"longitude":105.97417}], "phumy":[{"latitude":14.21639},{"longitude":109.11694}], "longxuyen":[{"latitude":10.37528},{"longitude":105.41833}], "tayninh":[{"latitude":11.36778},{"longitude":106.11917}]}
location1 = location[city]
url = "https://api.darksky.net/forecast/{apikey}/{latitude},{longitude}?exclude=currently,alerts,minutely,flags&{units}".format(apikey=apikey,latitude=location1[0]["latitude"],longitude=location1[1]["longitude"],units=units) 

res = requests.get(url).json()
# pprint(res)

data_hour = res["hourly"]["data"]
data_day = res["daily"]["data"]
temp_max = data_day[0]["apparentTemperatureHigh"]   # nhiet do trung binh cao nhat
temp_min = data_day[0]["apparentTemperatureLow"]    # nhiet do trung binh thap nhat
temp = data_hour[0]["apparentTemperature"]   # nhiet do trung binh hien tai
humidity = data_hour[0]["humidity"]  # do am khong khi
windSpeed = data_hour[0]["windSpeed"] # toc do gio

print("Nhiet Do: %d"%(round(temp, 0)))
print("Nhiet Do Cao Nhat Trong Ngay: %d"%(round(temp_max, 0)))
print("Nhiet Do Thap Nhat Trong Ngay: %d"%(math.floor(temp_min)))
print("Do Am: %s%s"%(humidity*100,"%"))
print("Toc Do Gio: %s km/h"%(windSpeed))

# print(location1[0]["latitude"])
# print(location1[1]["longitude"])