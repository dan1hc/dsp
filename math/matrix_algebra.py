# Matrix Algebra
import numpy as np
from collections import OrderedDict

A = np.array([(1,2,3),(2,7,4)])
print(A)
B = np.array([(1,-1),(0,1)])
print(B)
C = np.array([(5,-1),(9,1),(6,0)])
print(C)
print(C.transpose())
D = np.array([(3,-2,-1),(1,2,3)])
print(D)
u = np.array([6,2,-3,5])
print(u)
v = np.array([3,5,-1,4])
print(v)
w = np.array([1,8,0,5])
print(w[:, np.newaxis], '\n')
answers = OrderedDict([('1', np.nan), ('2', A-C.transpose()), ('3', D*3), ('4', B@A), ('5', np.nan), ('6', np.nan), ('7', C@B), ('8', B**4), ('9', A@A.transpose()), ('10', D.transpose()@D)])

for a in answers:
    print(a, answers[a], '\n')
