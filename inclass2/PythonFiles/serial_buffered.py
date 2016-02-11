import serial
import ringbuffer
import numpy as np
import time
import thread
import matplotlib
matplotlib.use('TKAgg')  # need to use this on OSX for animate w/ blit=True
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.lines import Line2D


BUFFER_SIZE = 500
data = ringbuffer.RingBuffer(BUFFER_SIZE)

serial_port = serial.Serial('/dev/tty.usbserial-A5027IRK', baudrate=57600, timeout=1)
serial_port.flush()

# setup the figure to plot with
fig = plt.figure()
fig.suptitle("ACTION", fontsize=12)
# setup the plot
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlim(0, BUFFER_SIZE-1)
ax1.set_ylim(0, 255)
line1 = Line2D([], [], color='red', linewidth=0.5)
ax1.add_line(line1)

# initialization, plot nothing (this is also called on resize)
def init():
    # called on first plot or redraw
    line1.set_data([], [])  # just draw blank background
    return line1,


# animation function.  This is called sequentially, after calling plt.show() (on main thread)
def animate(i):
    # generate some data to draw
    x = np.linspace(0, BUFFER_SIZE-1, BUFFER_SIZE)
    y = data.get_samples
    line1.set_data(x, y)

    y_max = max(y)
    y_min = min(y)
    delta = y_max - y_min

    if delta < 30:
        print("GROUND")
    elif delta < 60:
        print("NO TOUCH")
    elif delta < 100:
        print("HOVER")
    elif delta < 200:
        print("WIRE TOUCH")
    else:
        print("TOUCH")

    # return line(s) to be drawn
    return line1,

def read_serial_forever():
    global data
    while True:
        values = serial_port.read(10)
        if values:
            tmp = np.array([ord(value) for value in values])

            data.insert_new(tmp.astype(np.int16))
            #print np.sum(tmp)

        time.sleep(0.002)

thread.start_new_thread(read_serial_forever, () )

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig,  # the figure to use
                               animate,  # the function to call
                               init_func=init,  # the function to init the drawing with
                               frames=200,  # the max value of "i" in the animate function, before resetting
                               interval=20,  # 20 ms between each call
                               blit=True)  # do not redraw anything that stays the same between animations

# this is a blocking call that will sequentially call the animate function
plt.show()

'''for i in range(0, 10):
    time.sleep(1)
    print "sleeping", i'''

serial_port.close()
