import numpy as np
from numpy.linalg import svd


n = 4
Dx = np.array([2,4,6])
Dy = np.array([1,2,3])
Dz = np.array([1,2,3])
Db = np.array([1,1,1])
YY = np.array([3,6,9])

dataSet = np.array([Dx, Dy, Dz, Db])
alpha = np.array([[np.average(i*j)for i in dataSet] for j in dataSet])

arr_Y = [ np.average(i) for i in YY * dataSet]


alpha_p = np.linalg.pinv(alpha)

ans  = alpha_p.dot(arr_Y)
print(ans)

# U, Sigma, VT = svd(alpha, full_matrices=True)
# Sigma = np.diag(Sigma)
# UT = np.transpose(U)
# V = np.transpose(VT)

# print(alpha.dot(V).dot(np.transpose(Sigma)).dot(UT))
