from machine import Pin
from machine import PWM
import time



def dimmer(pn, level):
    p = Pin(pn)
    tim = PWM(0, frequency=100)
    ch = tim.channel(2, duty_cycle=level, pin=p)
