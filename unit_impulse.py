import numpy as np
import matplotlib.pyplot as plt

def sin(x):
    return np.sin(x)

n = 50 # 중첩횟수

pi = np.pi
t = np.arange(0,5,0.001)

x = sin(2*pi*t)
for i in range(1,n):
    x += sin((4*i+2)*pi*t)/(2*i+1) 

plt.figure(figsize=(10,2))
plt.plot(t,x)
plt.show()