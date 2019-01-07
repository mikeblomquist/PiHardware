from gpiozero import LED
from time import sleep
import threading

led = LED(17)

class beeperTest(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        print('thread started')
        print (self.name)
        while True:
            led.on()
            sleep(1)
            led.off()
            sleep(1)
