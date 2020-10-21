#lab1
#203130851

import numpy as np

#q1
a = np.full((4,4), 2)
for i in range(4):
    a[i, i] = 5
print(a)

#q2
b = np.full((5,5), 5)
b[1:4, 1:-1] = 0
b[2,2] = 1
print(b)

#q3
c = np.full((3,3), 2)
d = np.full((3,3), 8)
print(c+d)
print(d-c)
print(c*d)
print(d/c)

#q4
mat = np.array([[1,1,2],
                [2,1,0],
                [1,2,2]])

solVec = np.array([[1],[2],[3]])
invMat = np.linalg.inv(mat)
xyz = invMat @ solVec
print(xyz)