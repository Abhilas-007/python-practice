pos=-1
def search(list,find):
    for i in list:
        if i==find:
            globals()['pos']=list.index(i)
            return True
    return False
size=int(input("Enter the size of list"))
print("Enter the elements of list")
list=[]
for i in range(size):
    list.append(int(input()))

find=int(input("Enter the element to search"))

if search(list,find):
    print("Found at ",pos)
else:
    print("Not found")