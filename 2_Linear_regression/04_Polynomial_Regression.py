import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# from sympy import symbols, diff
# from numpy.linalg import svd
# from numpy.core.fromnumeric import transpose
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4]) #서수 표현

# Data settings.
n = 30  # The number of data
w1,w2 = -1,1 # x-axis, Start and End points.
data_X = np.linspace(w1,w2,n) 
data_Y = data_X**3 -8* data_X**2 - 2*data_X +  np.random.rand(n)*4

# Graph settings.
fig, ax1 = plt.subplots(nrows = 1, ncols = 1)
ax1.set_ylim(min(data_Y), max(data_Y))
ax1.scatter(data_X, data_Y)
text = ax1.text(0,-4,'')
line, = ax1.plot([],[])




def update(N):
    yArray = np.array([ np.average(data_Y * data_X**i) for i in range(N)] )
    xArray = np.array([[ np.average(data_X**(i+j)) for i in range(N) ] for j in range(N)])

    xx=np.linalg.inv(xArray)
    result = xx.dot(yArray)


    xx = np.linspace(w1,w2,100)
    yy = [0 for _ in xx]
    for i in range(N):
        yy += result[i]*xx**i

    line.set_data(xx,yy)
    text.set_text(str(ordinal(N))+' degree' )
    

    if N in [3]:
        ax1.plot(xx,yy)
   
    
# Animation

degreeNum = 30
ani = FuncAnimation(fig, update,range(1,degreeNum+1,1),interval=250,repeat=False) # Animation operator
plt.show()

# U, Sigma, V = svd(xArray)
# X = V.dot(Sigma).dot(U.T)
# X = X.dot(yArray)
# print(X)