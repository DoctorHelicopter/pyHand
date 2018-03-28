import datetime
from time import sleep
from picamera import PiCamera


def main():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    
    while True:
        raw_input("Press enter to take a picture")
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        filename = 'captures/{}.jpg'.format(timestamp)
        camera.capture(filename)
        print("Picture added! {}".format(filename))

if __name__=="__main__":
    main()
