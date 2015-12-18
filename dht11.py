# -*- coding: utf-8 -*-
"""
This is the code for DTH11 to get the humidity and temperature
"""

import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
time.sleep(1)
#用来接收收到的数据
data=[]
pin = 26
j=0
#start work
gpio.setup(pin,gpio.OUT)
#先给个低电平
gpio.output(pin,gpio.LOW)
time.sleep(0.02)
#再给个高电平
gpio.output(pin,gpio.HIGH)
i=1
i=1

#wait to response
#设置成in模式，即板子读这个pin脚的数据
gpio.setup(pin,gpio.IN)

while gpio.input(pin)==0:
    continue
while gpio.input(pin)==1:
        continue
#get data
#数据是40bit的
while j<40:
    k=0
    while gpio.input(pin)==0:
        continue
    #根据1的个数（即高电平的时间来判断是0还是1）
    while gpio.input(pin)==1:
        k+=1
        if k>100:break
    if k<3:
        data.append(0)
    else:
        data.append(1)
    j+=1

print "Sensor is working"
#get temperature
#下面就是处理接收到的数据
humidity_bit=data[0:8]
humidity_point_bit=data[8:16]
temperature_bit=data[16:24]
temperature_point_bit=data[24:32]
check_bit=data[32:40]

humidity=0
humidity_point=0
temperature=0
temperature_point=0
check=0



for i in range(8):
    humidity+=humidity_bit[i]*2**(7-i)
    humidity_point+=humidity_point_bit[i]*2**(7-i)
    temperature+=temperature_bit[i]*2**(7-i)
    temperature_point+=temperature_point_bit[i]*2**(7-i)
    check+=check_bit[i]*2**(7-i)

tmp=humidity+humidity_point+temperature+temperature_point
if check==tmp:
    print "temperature is ", temperature,"wet is ",humidity,"%"
    print "something is successful the humidity,humidity_point,temperature,temperature_point,check is",humidity,humidity_point,temperature,temperature_point,check
else:
    print "something is worong the humidity,humidity_point,temperature,temperature_point,check is",humidity,humidity_point,temperature,temperature_point,check