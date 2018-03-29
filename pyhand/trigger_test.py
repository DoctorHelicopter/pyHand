import time, datetime

import pigpio

from picamera import PiCamera

buttonPin = 14

def callback(gpio, level, tick):
    if level == 0: # button press
        take_picture()

def take_picture():  
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = 'captures/{}.jpg'.format(timestamp)
    camera.capture(filename)
    print("Picture added! {}".format(filename))

if __name__=="__main__":
    pi = pigpio.pi()
    if not pi.connected:
        exit()

    # Setup the button
    pi.set_mode(buttonPin, pigpio.INPUT)
    pi.set_pull_up_down(buttonPin, pigpio.PUD_UP)
    pi.set_glitch_filter(buttonPin, 5000) # 5000 micros debounce

    cb = pi.callback(buttonPin, pigpio.EITHER_EDGE, callback)

    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()

    while True: # all the work is done in the callback
        time.sleep(1)
