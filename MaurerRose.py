import math

import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')
from matplotlib import animation
import matplotlib.figure as figure
import matplotlib.axes._axes as axes
import matplotlib.lines as lines


def init():
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    return line, border,


def update(frame):
    if frame < 361:
        k = frame * d * (math.pi / 180)
        r = math.sin(n * k)

        x = r * math.cos(k)
        y = r * math.sin(k)

        # Append data
        x_data.append(x)
        y_data.append(y)

        # Set data
        line.set_data(x_data, y_data)
    else:
        frame -= 361

        k2 = frame * math.pi / 180
        r2 = math.sin(n * k2)

        x2 = r2 * math.cos(k2)
        y2 = r2 * math.sin(k2)

        x2_data.append(x2)
        y2_data.append(y2)

        border.set_data(x2_data, y2_data)

    return line, border,


fig = plt.figure()  # type:figure.Figure
ax = fig.add_subplot()  # type:axes.Axes

# Create line
line, = ax.plot([], [], lw=1)  # type:lines.Line2D
border, = ax.plot([], [], lw=2, color='r')

# Data lists
x_data, y_data, x2_data, y2_data = [], [], [], []

# Variables
n = 2
d = 29

ani = animation.FuncAnimation(fig, update, init_func=init, blit=True, frames=[x for x in range(0, 2*361)], interval=10,
                              repeat=False)

plt.show()
