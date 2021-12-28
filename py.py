import numpy as np
import matplotlib.pyplot as plt

data_x = np.array([1,2,3])
data_y = np.array([3,5,7])

def E(array):
    return np.average(array)

def Linear():
    x = data_x
    y = data_y

    a = (E(x*y) - E(x) * E(y)) / (E(x*x) - E(x) * E(x))
    b = E(y) - a * E(x)
    print(a,b)
    

Linear()