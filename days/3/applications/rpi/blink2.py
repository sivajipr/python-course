import time


#First, write '14' to /sys/class/gpio/export
#Write 'out' to /sys/class/gpio/gpio14/direction



def set_output(fd, val):
        fd.write(val)
        fd.flush()

def blink():
        fd = open('/sys/class/gpio/gpio14/value', 'w')
        while True:
                set_output(fd, '1')
                time.sleep(.1)
                set_output(fd, '0')
                time.sleep(.1)

