from machine import Pin, PWM
import math
from utime import sleep

#setup
light = Pin(15, Pin.OUT)
pwm = PWM(light, freq= 1000)
on = True
#loop
while on == True:
    for i in range(0, 65535):
        pwm.duty_u16(i)
        sleep(2/65535)
        

    for i in range(65535, 0, -1):
        pwm.duty_u16(i)
        sleep(1/65535)

