import numpy
#numpy.set_printoptions(legacy='1.13')
num='1 2 3 4 5 6'
array=numpy.array(list(num,))
num1='5 6 7 8 9 3'
array=numpy.append(array,num1)
print(array)
print(array.shape)
print(type(array))