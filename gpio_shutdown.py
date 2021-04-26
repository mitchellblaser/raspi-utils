import os
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(2) == GPIO.HIGH:
        print("Shutdown on GPIO.")
	os.system("sudo shutdown now")
