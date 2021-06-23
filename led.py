import RPi.GPIO as GPIO
import time

LED_RED = 11
LED_GREEN = 13
LED_BLUE = 15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)

def turn_on_red():
    GPIO.output(LED_RED,GPIO.HIGH)
    
def turn_on_green():
    GPIO.output(LED_GREEN,GPIO.HIGH)
    
def turn_on_blue():
    GPIO.output(LED_BLUE,GPIO.HIGH)
    
def turn_off_red():
    GPIO.output(LED_RED,GPIO.LOW)
    
def turn_off_green():
    GPIO.output(LED_GREEN,GPIO.LOW)
    
def turn_off_blue():
    GPIO.output(LED_BLUE,GPIO.LOW)

def blink_red():
    turn_on_red()
    time.sleep(0.1)
    turn_off_red()
    
def blink_green():
    turn_on_green()
    time.sleep(0.1)
    turn_off_green()
    
def blink_blue():
    turn_on_blue()
    time.sleep(0.1)
    turn_off_blue()