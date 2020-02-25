import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt
GPIO.cleanup()


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)



GPIO.output(12,1)
GPIO.output(15,0)



