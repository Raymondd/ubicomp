import serial, time, random
from matplotlib import pyplot as plt
import numpy as np

class serialPort():
    def __init__(self, port):
        #self.ser = serial.Serial('/dev/tty.usbmodem1412', 9600, timeout=1)
        #self.flush()
        print("init")

    def write(self, payload):
        self.ser.write(payload + '\r\n')
        time.sleep(1)

    def read(self):
        payload = self.ser.read()
        print payload
        #return a casted integer type
        return ord(payload)

    def movingTimeSeries(self, size):
            self.tsData = [-1 for i in range(size)]
            self.ax = plt.axes(xlim=(0, 20), ylim=(0, 10))
            self.line, = plt.plot(self.tsData)
            plt.ion()  # interactive plots can do not block on "show"
            plt.show()  # show the plot on the screen

    def updateTS(self, point):
        self.tsData.insert(0, point)
        self.tsData.pop()
        self.line.set_ydata(self.tsData)  # set the data
        plt.draw()  # and draw it out
        time.sleep(0.1)  # simulate some down time
        plt.pause(0.0001)  # pause so that the drawing updates

    def graph(self, x, y):
        #sample x and y in numpy
        # 100 equally spaced array of numbers from 0.0 to 1
        #x = np.linspace(0, 1, 100)
        # take sine of the value
        #y = np.sin(2 * 3.14159 * t)
        plt.plot(x, y)  # plot them
        plt.show()

    def close(self):
        self.ser.close()


if __name__ == '__main__':
    #example of polling from a serial port
    ser = serialPort('myPort')
    ser.movingTimeSeries(50)

    for i in range(100):
        #read from serial port here
        ser.updateTS(random.randint(1, 10))


    print("hello world")
