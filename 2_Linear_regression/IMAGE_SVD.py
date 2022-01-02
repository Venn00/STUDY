# module import
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

im = Image.open('img.jpg')

# # transform original image: gray scale
im = im.convert('I')
# ruby_arr = np.array(im) # shape: (3024, 4032)

fig, ax = plt.subplots()
ax.imshow(im, cmap='gray')

# svd
U, Sigma, VT = np.linalg.svd(im)


def update(i):
    im2 = U[:,:i].dot(np.diag(Sigma[:i])).dot(VT[:i,])    
    # fig.canvas.draw_idle()
    ax.imshow(im2, cmap='gray')
    plt.title(i)

maxN = len(Sigma)

array = [1,1,1]
while array[-1] < maxN: array.append(array[-3]+array[-2])
ani = FuncAnimation(fig, update,array,interval=250,repeat=False) # Animation operator
plt.show()

