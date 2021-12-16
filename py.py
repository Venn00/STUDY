import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x = np.arange(-10,10,0.1)
y = x ** 2 * np.sin(x)
# y = x ** 2

ax.set_xlim(min(x),max(x))
ax.set_ylim(min(y),max(y))
plt.plot(x,y)

x, y = [2.5], [1]
line, = plt.plot([], [], 'bo')

def f(x):
    return x ** 2 * np.sin(x)
    # return x ** 2

def diff_f(x):
    # return 2 * x
    return 2 * x * np.sin(x) + x ** 2 * np.cos(x)

def update(frame):
    print(x[-1])
    xx = x[-1] - diff_f(x[-1]) * 0.01
    yy = f(xx)
    x.append(xx)
    y.append(yy)
    print(xx,diff_f(x[-2]),yy)
    line.set_data(x[1::], y[1::])


ani = FuncAnimation(fig, update, frames = list(range(1,2)))
plt.show()