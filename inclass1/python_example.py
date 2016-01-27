#! /usr/bin/python


# this is a comment

"""this is a multiple
line comment"""

# ============================================
# Variables Example
int_val = 8
long_val = 23423423235L
float_val = 2.0
bool_val = True

print "Variable type examples:"
print type(int_val)
print type(long_val)
print type(float_val)
print type(bool_val)

#============================================
# Arithmetic and casting
print "\nArithmetic examples:"
print 8 / 3
print float(8) / 3
print float(8) / float(3)

print True and False
print 8 == 3
print 5 <= 6

#============================================
# string example
print "\nString example:"
str_val = "A string is double or single quotes"
str_val_long = '''Three quote means that the string goes over
multiple lines'''
str_val_no_newline = '''This also spans multiple lines \
but has no newline'''

print str_val
print str_val_long
print str_val_no_newline

#============================================
# for loop example with list
print "\nfor loop output:"

list_example = [int_val, long_val, float_val, bool_val]
list_example.insert(0, "UbiComp")

for val in list_example:
    print str(val) + ' ' + str(type(val))

#============================================
# array as a stack
print "\nStack Example:"
list_example = []
list_example.append('LIFO')

for i in range(0, 5):
    list_example.append(i)

print list_example
print "============="
val = list_example.pop()
print val
print "============="
print list_example
print "============="

#============================================
# array as a queue
print "\nQueue Example:"
from collections import deque

q_example = deque()
q_example.appendleft("FIFO")
for i in range(5, 10):
    q_example.appendleft(i)

print q_example
print "============="
val = q_example.pop()
print val
print "============="
print q_example
print "============="

# pop and print each element
while len(q_example) > 0:
    print q_example.pop()

#============================================
# conditional example
print "\nConditional Example:"
a, b = True, False

if a:
    print "a is true"
elif a or b:
    print "b is true"
else:
    print "neither a or b are true"

# conditional assignment
val = "b is true" if b else "b is false"
print val

#============================================
print "\nFunction Example:"
# create and call a function
# the function can be defined almost anywhere in file, as long as it is before it gets used
def make_strings_lowercase(str_input):
    assert isinstance(str_input, str)  # test the type of input
    return str_input.lower()

# now we are back on the main execution
print make_strings_lowercase("UPPER CASE")
print make_strings_lowercase("UbiComp")

#============================================
# plotting example
from matplotlib import pyplot as plt
import numpy as np

t = np.linspace(0, 1, 100)  # 100 equally spaced array of numbers from 0.0 to 1
y = np.sin(2 * 3.14159 * t)  # take sine of the value

plt.plot(t, y)  # plot them
plt.show()


#============================================
# plotting in real time example

import time  # for sleeping
import random  # for generating random data

# create a queue of size N
size_of_queue = 25
init_queue_value = -1
data = deque([init_queue_value] * size_of_queue)

# setup the plot
# show at 0:20 on the x axis and 0:10 on y axis
ax = plt.axes(xlim=(0, 20), ylim=(0, 10))
line, = plt.plot(data)  # get handle to the "line" that we use for updating the plot

plt.ion()  # interactive plots can do not block on "show"
plt.show()  # show the plot on the screen

# do this until the queue is all filled in
for i in range(0, len(data)):
    # get a random number
    # and add number to the queue
    data.appendleft(random.randint(1, 10))
    data.pop()  # pop the last number off to keep queue size the same

    line.set_ydata(data)  # set the data
    plt.draw()  # and draw it out

    time.sleep(0.1)  # simulate some down time
    plt.pause(0.0001)  # pause so that the drawing updates


#============================================
# Serial reading example
import serial

serial_port = serial.Serial('/dev/tty.usbmodem1412', 9600, timeout=1)
serial_port.flush()

while True:
    # default behavior is to return a string
    val = serial_port.read()
    if val:
        value_as_int = ord(val)
        print val, type(val), value_as_int

        if value_as_int >= 30:
            break  # break from the loop

serial_port.close()