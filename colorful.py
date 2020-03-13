'''
Sample program.
Change LED color every time button is pressed.
'''
from Maix import GPIO
from fpioa_manager import *

fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
but_a = GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)

fm.register(board_info.LED_R, fm.fpioa.GPIO2)
fm.register(board_info.LED_G, fm.fpioa.GPIO3)
fm.register(board_info.LED_B, fm.fpioa.GPIO4)

led_r = GPIO(GPIO.GPIO2, GPIO.OUT)
led_g = GPIO(GPIO.GPIO3, GPIO.OUT)
led_b = GPIO(GPIO.GPIO4, GPIO.OUT)

led_r.value(0)
led_g.value(1)
led_b.value(1)

prev_but = 1
counter = 0
while True:
    curr_but = but_a.value()
    if prev_but != curr_but and curr_but==0:
        counter += 1
        led_r.value((counter%3)!=0)
        led_g.value((counter%3)!=1)
        led_b.value((counter%3)!=2)
    prev_but = curr_but