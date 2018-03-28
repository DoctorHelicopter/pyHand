import pigpio
import time

buttonPin = 14

def callback(gpio, level, tick):
    if level == 0: # button press
        print("button pressed")

pi = pigpio.pi()
if not pi.connected:
   exit()


# Setup the button
pi.set_mode(buttonPin, pigpio.INPUT)
pi.set_pull_up_down(buttonPin, pigpio.PUD_UP)
pi.set_glitch_filter(buttonPin, 5000) # 5000 micros debounce

cb = pi.callback(buttonPin, pigpio.EITHER_EDGE, callback)

while True: # all the work is done in the callback
   time.sleep(1)