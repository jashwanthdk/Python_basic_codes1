from numpy import *
arr = array([1,2,3,4,5])
print(arr)
print(arr.dtype)

arr= array([1,2,3,4,5.0])
print(arr)

arr = linspace(0,15,20)
print(arr)
# from 0 to 15 dividing into 20 equal parts

arr = arange(0,10,2)
print(arr)
# incrementin gfrom 0 to 10 by 2 steps

arr = logspace(0,16,15)
print(arr)
# from 10power0 to 10power16 diving into 15 parts each

print('%.2f' %arr[14])
arr=ones(5,'int')
print(arr)
arr = zeros(5)
print(arr)