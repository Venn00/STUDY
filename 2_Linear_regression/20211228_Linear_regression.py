# First Order System
# #Mean Square Error
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

n = 50 # Number of data samples
data_x = np.random.rand(n)
G = 2 # Gradiant
data_y = data_x * G + np.random.rand(n) 

#initializing
a, b = [np.average(data_x)],[np.average(data_y)] #initial variable.

#Graph Initializing
fig, [ax1, ax2] = plt.subplots(nrows = 2, ncols = 1)

#Ax1 : scatter & line
dot = ax1.scatter(data_x,data_y)
line, = ax1.plot([],[])

text = ax1.text(0.4,0.5,'') # text Ax + B

#Ax2 : scatter & x,ylim
dot2 = ax2.scatter([],[])
ax2.set_xlim(-0.1,0.1)
ax2.set_ylim(-0.4,0.4)
ax2.grid(True)

#Learning rate
lr = 0.3

# Scatter add a point
def addPoint(scat, new_point, c='k'): 

    old_off = scat.get_offsets()
    new_off = np.concatenate([old_off,np.array(new_point, ndmin=2)])
    # old_c = scat.get_facecolors()
    # new_c = np.concatenate([old_c, np.array(matplotlib.colors.to_rgba(c), ndmin=2)])

    scat.set_offsets(new_off)
    # scat.set_facecolors(new_c)

    scat.axes.figure.canvas.draw_idle()


# Animation function
def update(frame):

    A = a[-1]
    B = b[-1]

    x = [v for v in range(2)]
    y = [w * A + B for w in range(2)]

    da = np.sum(data_x*A*(data_y - (A * data_x + B)))/n
    db = np.sum((data_y - (A * data_x + B) ))/n
    
    text.set_text('Current Val :   Y =  '+ str(A)[0:5] +'  X  +  '+ str(B)[0:5])

    a.append(A + da*lr)
    b.append(B + db*lr)

    line.set_data(x,y)
    addPoint(dot2,[da,db])


# Linear_regression

def E(array):
    return np.average(array)

def Linear():
    x = data_x
    y = data_y
    a = (E(x*y) - E(x) * E(y)) / (E(x*x) - E(x) * E(x))
    b = E(y) - a * E(x)

    ax1.text(0.4,0.8,'Assumption :  Y =  '+ str(a)[0:5] +'  X  +  '+ str(b)[0:5])

    ax1.plot([0, 1], [0 * a + b , 1 * a + b])
    ax2.scatter(0,0)

Linear()
ani = FuncAnimation(fig, update,interval=10) # Animation operator

plt.show()