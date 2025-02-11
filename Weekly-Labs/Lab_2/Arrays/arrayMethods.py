# from array import *

# numbers = array('i', [1,2,3,4,5,6,7,8,9,10])

# #slicing in arrays

# print(numbers[0:5]) #prints first 5 elements
# print(numbers[5:]) #prints elements from index 5 to the end
# print(numbers[:5]) #prints elements from the start to index 5
# print(numbers[0:5:2]) #prints elements from index 0 to 5 with a step of 2
# print(numbers[::2]) #prints all elements with a step of 2



import numpy as np

#creating an array
# a = np.array([[1,2,3,4,5],[4,5,5,7,89]])
# print(a[0,1])


# a= np.array([1,2,3,4,3,5], ndmin=5)
a = np.array([[1,2,3,4,3,5], [1,2,3,4,3,5]])
# newar = a.reshape(12)
# newar = a.reshape(12)
# print(newar)

for x in np.nditer(a):
    print(x)



# b = np.array([1,2,3,4,5,6,7,8,9,10], dtype='S')

# print(b)