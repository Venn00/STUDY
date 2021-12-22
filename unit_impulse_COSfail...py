import numpy as np
import matplotlib.pyplot as plt

def cos(x):
    return np.cos(x)
def sin(x):
    return np.sin(x)

n = 10 # 중첩횟수

pi = np.pi
t = np.arange(0,5,0.001)

x = cos(2*pi*t)

for i in range(1,n):
    x += 2 * sin(pi/3*i)/(pi-i) * cos(2*pi*i*3*1)

plt.figure(figsize=(10,2))
plt.plot(t,x)
plt.show()