from gpiozero import Button, LED
from time import sleep

# Pin definitions
button = Button(4, bounce_time=0.05)
led = LED(12)
led_pin.off()
def button_pressed():
    led.toggle()
    pass
button.when_pressed = button_pressed

try:
    while True:
        sleep(0.01)

finally:
    button.close()
    led.close()