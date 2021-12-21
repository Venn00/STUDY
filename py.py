import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x): # 기본식
    return x ** 2 * np.sin(x)

def df_f(x): #적분식
    return 2 * x * np.sin(x) + x ** 2 * np.cos(x)

fig, ax = plt.subplots()

x = np.arange(-10,10,0.1)
y = f(x)
init = -6 # 초기값.

ax.set_xlim(min(x),max(x))
ax.set_ylim(min(y),max(y))
plt.plot(x,y)

line, = plt.plot([], [], 'bo')

x, y = [init], [f(init)]

line2, = plt.plot(x,y,'ro')

def update(frame):
    print(x[-1])
    xx = x[-1] - df_f(x[-1]) * 0.01
    yy = f(xx)
    line2.set_data(xx,yy)
    x.append(xx)
    y.append(yy)
    line.set_data(x,y)


ani = FuncAnimation(fig, update,)
plt.show()