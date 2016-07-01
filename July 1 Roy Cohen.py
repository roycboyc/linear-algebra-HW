##question 8

A = np.array([[1,2,3,4,5],
     [1,2,3,4,5],
     [1,2,3,4,5],
     [1,2,3,4,5],
     [1,2,3,4,5]])

result = A**3   
##question 9

import numpy as np

matA = np.array ([[2,4,5],
     [2,6,1],
     [-2,9,15],
     [12,0,15],
     [3,34,-52]])

matB = np.array ([[2,3,4,5],
        [2,6,1,4],
        [-2,9,15,4]])

matC = np.dot(matA,matB)

matReturn = np.transpose(matC)

##question 10
from numpy.linalg import matrix_rank
M = np.array([[2,4,5],
     [2,6,1],
     [-2,9,15],
     [12,0,15],
     [3,34,-52]])

mRank = matrix_rank(M)

##question 11
import sympy
M = np.array ([[1,0,1,3],[2,3,4,7],[-1,-3,-3,-4]])
print sympy.Matrix(M).rref()