from numpy import *

arr1 = array([[1,2,3,4,5,6],[2,3,4,5,6,7]])
print(arr1)

print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

arr2= arr1.flatten()
print(arr2)

arr3 = arr1.reshape(3,4)
print(arr3)

arr3=arr1.reshape(2,2,3)
print(arr3)

m = matrix(arr1)
print(m)
n = matrix('1,2;3,4;5,6')
print(n)