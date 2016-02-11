import serial, ringbuffer, time, thread, matplotlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.lines import Line2D
matplotlib.use('TKAgg')  # need to use this on OSX for animate w/ blit=True


BUFFER_SIZE = 128
data = ringbuffer.RingBuffer(BUFFER_SIZE)

serial_port = serial.Serial('/dev/tty.usbserial-A5027IRK', baudrate=57600, timeout=1)
serial_port.flush()


# setup the figure to plot with
fig = plt.figure()

# setup the plot
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlim(0, BUFFER_SIZE-1)
ax1.set_ylim(0, 255)
line1 = Line2D([], [], color='red', linewidth=0.5)
ax1.add_line(line1)

#setup the frequency plot
ax2 = fig.add_subplot(2, 1, 2)
ax2.set_xlim(0, audio.rate)
ax2.set_ylim(-50, 100)
line2 = Line2D([], [], color='blue', linewidth=0.5)
ax2.add_line(line2)


def read_serial_forever():
    global data
    while True:
        values = serial_port.read(10)
        if values:
            tmp = np.array([ord(value) for value in values])

            data.insert_new(tmp.astype(np.int16))
            print np.sum(tmp)

        time.sleep(0.01)

# initialization, plot nothing (this is also called on resize)
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2


# animation function.  This is called sequentially, after calling plt.show() (on main thread)
def animate(i):
    # generate some data to draw
    y = data.get_samples
    x = np.linspace(0, BUFFER_SIZE-1, BUFFER_SIZE)
    line1.set_data(x, y)

    # now take the FFT of the data
    y_fft_raw = np.fft.rfft(y, BUFFER_SIZE)

    y_fft = 20*np.log10(np.abs(y_fft_raw))
    freq = np.linspace(0, audio.rate, len(y_fft))

    line2.set_data(freq, y_fft)
    # return line(s) to be drawn
    return line1, line2

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

serial_port.close()
