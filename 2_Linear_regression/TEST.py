# module import
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# load image
ruby = Image.open('img.jpg')

# transform original image: gray scale
ruby_gray = ruby.convert('I')
plt.imshow(ruby_gray)
ruby_arr = np.array(ruby_gray) # shape: (3024, 4032)

# SVD
u, sigma, vt = np.linalg.svd(ruby_arr)

# reconstruct image
# for i in range(1, 6):
i = 12
# reconstructed_ruby = u[:, :i] @ np.diag(sigma[:i]) @ vt[:i, :]
reconstructed_ruby = u[:,:i].dot(np.diag(sigma[:i])).dot(vt[:i,])
plt.imshow(reconstructed_ruby, cmap='gray')
plt.title(f"reconstructed image when t={i}")
plt.show()