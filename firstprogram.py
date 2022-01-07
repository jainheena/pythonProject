import numpy
from numpy import *
arr1 = matrix(input("enter your first 2d array n get new row by entering semi-colon(;): "))
arr2 = matrix(input("enter your second 2d array n get new row by entering semi-colon(;): "))
k = arr1.shape
n1 = k[0]
m1 = k[1]
v = arr2.shape
n2 = v[0]
m2 = v[1]
tu = n1*m2
arr3 = numpy.arange(tu).reshape(n1, m2)
for i in range(n1):
    for j in range(m2):
        x = 0
        for k in range(m1):
            x = x + (arr1[i, k] * arr2[k, j])
            arr3[i, j] = x
print(arr3)




