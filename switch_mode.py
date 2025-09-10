from machine import Pin,PWM
from utime import sleep
#funtions
mode = 0
def toggle_mode(hi):
    #button press changes mode value
    global mode
    mode = mode + 1
    print(mode)
    if mode >= 3:
        mode = 0
    
                
    

def light_on(light):
    pwm = PWM(light, duty_u16= 65535)
   

def light_fade(light):
    light.value(0)
    for i in range(0, 65535):
        pwm = PWM(light, freq = 1000, duty_u16=i)
        sleep(1/65535)
            

    for i in range(65535, 0, -1):
        pwm = PWM(light, freq= 1000, duty_u16=i)
        sleep(1/65535)




#setup
light = Pin(15, Pin.OUT)
detection = Pin(14, Pin.IN, Pin.PULL_UP)
detection.irq(trigger= light.IRQ_FALLING, handler = toggle_mode)
#loop
while True:
    while mode == 1:
        light_on(light)
    while mode == 2:
        light_fade(light)