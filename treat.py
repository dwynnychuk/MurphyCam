import RPi.GPIO as GPIO
import time


class Treat:
    """Dispense treat with servo"""
    servoPIN = 17
    pwmStart = 5
    pwmEnd = 10
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50)
    p.start(2.5)
    # getting to here and not initializing -> troubleshoot
    
    
    def __init__(self,p,pwmStart,pwmEnd):
        self.pwmStart = pwmStart
        self.pwmEnd = pwmEnd
        p.ChangeDutyCycle(pwmStart)
        time.sleep(0.5)
        p.ChangeDutyCycle(pwmEnd)
        time.sleep(0.5)


