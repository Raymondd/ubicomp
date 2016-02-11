import serial
import ringbuffer
import numpy as np
import time
import thread


BUFFER_SIZE = 128
data = ringbuffer.RingBuffer(BUFFER_SIZE)

serial_port = serial.Serial('/dev/tty.usbserial-A5027IRK', baudrate=57600, timeout=1)
serial_port.flush()


def read_serial_forever():
    global data
    while True:
        values = serial_port.read(10)
        if values:
            tmp = np.array([ord(value) for value in values])

            data.insert_new(tmp.astype(np.int16))
            print np.sum(tmp)

        time.sleep(0.01)

thread.start_new_thread(read_serial_forever, () )

for i in range(0, 10):
    time.sleep(1)
    print "sleeping", i

serial_port.close()