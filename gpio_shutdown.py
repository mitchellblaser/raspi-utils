import os
import time
import RPi.GPIO as GPIO

pin = 40

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

last_input = 0

while True:
    time.sleep(0.5)
    if GPIO.input(pin) == GPIO.HIGH:
        if last_input == 1:
            print("Shutdown on GPIO.")
            os.system("sudo shutdown now")
        last_input = 1
    else:
        last_input = 0
