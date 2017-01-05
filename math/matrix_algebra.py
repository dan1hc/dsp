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
w = np.array([1,8,0,5])[:, np.newaxis]
print(w, '\n')
answers = OrderedDict([
                       ('1.1', A.shape),
                       ('1.2', B.shape),
                       ('1.3', C.shape),
                       ('1.4', D.shape),
                       ('1.5', (1, 4)),
                       ('1.6', w.shape),
                       ('2.1', u+v),
                       ('2.2', u-v),
                       ('2.3', 6*u),
                       ('2.4', np.dot(u,v)),
                       ('2.5', np.linalg.norm(u)),
                       ('3.1', np.nan), 
                       ('3.2', A-C.transpose()), 
                       ('3.3', D*3), 
                       ('3.4', B@A), 
                       ('3.5', np.nan), 
                       ('3.6', np.nan), 
                       ('3.7', C@B), 
                       ('3.8', B**4), 
                       ('3.9', A@A.transpose()), 
                       ('3.10', D.transpose()@D)
                       ])

for a in answers.items():
    print(a, '\n')
    
"""
ANSWERS (also completed by hand, but I have no scanner)
('1.1', (2, 3)) 

('1.2', (2, 2)) 

('1.3', (3, 2)) 

('1.4', (2, 3)) 

('1.5', (1, 4)) 

('1.6', (4, 1)) 

('2.1', array([ 9,  7, -4,  9])) 

('2.2', array([ 3, -3, -2,  1])) 

('2.3', array([ 36,  12, -18,  30])) 

('2.4', 51) 

('2.5', 8.6023252670426267) 

('3.1', nan) 

('3.2', array([[-4, -7, -3],
       [ 3,  6,  4]])) 

('3.3', array([[ 9, -6, -3],
       [ 3,  6,  9]])) 

('3.4', array([[-1, -5, -1],
       [ 2,  7,  4]])) 

('3.5', nan) 

('3.6', nan) 

('3.7', array([[ 5, -6],
       [ 9, -8],
       [ 6, -6]])) 

('3.8', array([[1, 1],
       [0, 1]])) 

('3.9', array([[14, 28],
       [28, 69]])) 

('3.10', array([[10, -4,  0],
       [-4,  8,  8],
       [ 0,  8, 10]])) 
"""
    
    
