import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(111)

def animate(fig, ax):
    xdata, ydata = [], []
    ln, = ax.plot([], [], 'ro')

    def init():
        nonlocal ax
        ax.set_xlim(0, 2*np.pi)
        ax.set_ylim(-1, 1)
        return ln,

    def update(frame):
        nonlocal xdata, ydata, ln
        if xdata:
            xdata.pop()
        if ydata:
            ydata.pop()
        xdata.append(frame)
        ydata.append(np.sin(frame))
        ln.set_data(xdata, ydata)
        return ln,

    FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                  init_func=init, blit=True)
    plt.show()


animate(fig, ax)
