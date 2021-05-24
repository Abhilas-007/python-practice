from array import *
arr=array('i',[2,3,4,1,5])
#i-integers signed
#I-integers unsigned
#l-iong signed
#L-long unsigned
#f-float
#d-double
#h-short signed
#H-short unsigned
#b-char signed
#B-char unsigned
for i in range(len(arr)):
    print(arr[i])
print("----------------------")
for e in arr:
    print(e)
print("------------------")
newArr=array(arr.typecode,(a for a in arr))
for e in newArr:
    print(e)
#arrays are dynamic we use append() to add value and remove to remove values and typecode to know type of array
#arrays can be of single type and not like list