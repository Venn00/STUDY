from re import X
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from sympy import symbols, diff


N = 3
symbollist = []
for i in range(N+3):
    symbols(chr(65+i))
a,b,c,x,y = symbols('a,b,c,x,y')

f = (a*x**2 + b*x + c - y)**2
dfda = diff(f,a)
dfdb = diff(f,b)
dfdc = diff(f,c)


n = 8 # the number of data
q,w,e = 1.211, -1.111, 5.555
data_x = np.linspace(-3, 3, n) + np.random.rand(n)*0.3
data_y = q * data_x ** 2 + w * data_x + e + np.random.rand(n)*2



fig, ax1 = plt.subplots(nrows = 1, ncols = 1)
ax1.set_xlim(-4,4)
ax1.set_ylim(min(data_y)-2,max(data_y)+2)
ax1.scatter(data_x,data_y)




line, = ax1.plot([],[])


text1 = ax1.text(0,10,'')
text2 = ax1.text(0,9,str(q)[:5] + ' X^2 ' + str(w)[:5] +' X + ' + str(e)[:5])

lr = 0.01
A,B,C = 0,0,0
x1 = np.linspace(-5, 5, 30)
y1 = A * x1**2 + B * x1 + C 


def update(frame):
    global A,B,C
    A -= np.sum(list(map(lambda xx, yy: dfda.subs({x:xx, y:yy, a:A, b:B, c:C}) , data_x , data_y))) / n * lr
    B -= np.sum(list(map(lambda xx, yy: dfdb.subs({x:xx, y:yy, a:A, b:B, c:C}) , data_x , data_y))) / n * lr
    C -= np.sum(list(map(lambda xx, yy: dfdc.subs({x:xx, y:yy, a:A, b:B, c:C}) , data_x , data_y))) / n * lr
    y2 = A * x1**2 + B * x1 + C 
    line.set_data(x1,y2)
    text1.set_text(str(A)[:5] + ' X^2 ' + str(B)[:5] +' X + ' + str(C)[:5])
    
   
        


ani = FuncAnimation(fig, update,interval=10) # Animation operator

plt.show()

