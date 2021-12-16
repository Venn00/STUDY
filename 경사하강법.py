from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# ax.set_xlim()

# x = np.arange(-10,10,0.1)
# y = x ** 2 * np.sin(x)
# plt.figure()


line, = plt.plot([],[])
# 초기값. 
A , B = [1], []
l = 0.2

def update(a):
    print(a)
    aa = 2 ** a * np.sin(a) + a **2 * np.cos(a)
    a = a - l * aa
    B.append(a ** 2 * np.sin(a))
    A.append(a)
    line.set_data(A[1::],B)
    return line,

ani = FuncAnimation(fig, update(A[-1]), frames = np.linspace(1,100))



plt.show()
