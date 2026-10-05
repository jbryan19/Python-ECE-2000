#!/usr/bin/python
# button.py
# Description: When you press the button, the LED turns on
# Author:Jack Bryan

import time
import gpiozero as GPIO
dTime = 0
def press_time():
    counter = 0
    cTime = time.time()
    while btn_pin.is_pressed:
        continue
    eTime = time.time()
    dTime = eTime-cTime
    print(dTime)
    return dTime

# Pins definitions
btn_pin = GPIO.Button(4)
led_pin = GPIO.LED(12)

# If button is released, light up LED
try:
    while True:
        
        if btn_pin.is_pressed:
             dTime = press_time()
        if dTime < 1.0:
            led_pin.on()
    
        elif 1.0 <= dTime <= 3.0:
            led_pin.on()
            time.sleep(0.1)
            led_pin.off()
            time.sleep(0.1)
            
        else:
            led_pin.off()
           
# When you press ctrl+c, this will be called
finally:
    led_pin.close()
    btn_pin.close() 
