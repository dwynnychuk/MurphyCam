class Treat:
    """Dispense treat with servo"""

    def __init__(self, num_treat):
        servoPIN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)

        p = GPIO.PWM(servoPIN, 50)
        p.start(2.5)
        pwmStart = 5
        pwmEnd = 10
        
        for i in range(num_treat):
            p.ChangeDutyCycle(pwmStart)
            time.sleep(0.5)
            p.ChangeDutyCycle(pwmEnd)
            time.sleep(0.5)


