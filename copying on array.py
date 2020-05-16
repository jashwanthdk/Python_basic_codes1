from numpy import *

arr1 = array([1,2,3,4,5])
arr2 = array([3,4,5,6,6])
arr3 = arr1 + arr2
print(arr3)

print(sin(arr3))
print(cos(arr3))
print(sqrt(arr3))
print(sum(arr3))
print(min(arr3))
print(max(arr3))
print(concatenate([arr1,arr2]))

arr4 = array([2,3,4,5,6])
arr5 = arr4.view()
print(arr4)
print(arr5)
print(id(arr4))
print(id(arr5))

#two types of copying shallow copying nd deep copying
# after arr5 = arr4
#the elements are same in both of the arrays and their address is also the same
#the elements after arr5=arr4.view() the ids are different

# if me make a change in one of the array the values get changed in both arrays this is called shallow copying
# after making one change in a single array the copied arrray remains intact this is called deep copying

arr5 = arr4.copy()
#deep copying
print(id(arr5))
print(id(arr4))
