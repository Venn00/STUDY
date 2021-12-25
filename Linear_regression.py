# First Order System.
# Mean Square Error
# Variance

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

n = 30 # Number of data samples
data_x = np.random.rand(n)
G = 2 # Gradiant
data_y = data_x * G + np.random.rand(n) 

#initializing
a, b = [np.average(data_x)],[np.average(data_y)] #initial variable.

#Graph Initializing
fig = plt.figure()
plt.scatter(data_x,data_y)
line, = plt.plot([],[])

#Learning rate
lr = 0.01

def update(frame):

    A = a[-1]
    B = b[-1]

    x = [v for v in range(2)]
    y = [w * A + B for w in range(2)]

    line.set_data(x,y)

    da = np.sum(data_x*A*(data_y - (A * data_x + B)))
    db = np.sum((data_y - (A * data_x + B) ))
    plt.title('Y =  '+ str(A)[0:4] +'  X  +  '+ str(B)[0:4])
    a.append(A + da*lr)
    b.append(B + db*lr)
    




ani = FuncAnimation(fig, update,interval=10)

plt.show()