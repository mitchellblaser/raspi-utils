import os
import time
import RPi.GPIO as GPIO

pin = 40

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    time.sleep(0.05)
    if GPIO.input(pin) == GPIO.HIGH:
        print("Shutdown on GPIO.")
        os.system("sudo shutdown now")
