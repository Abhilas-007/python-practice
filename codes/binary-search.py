pos=-1
def search(list,find):
    l=0
    u=len(list)-1

    while l<=u:
        mid=(l+u)//2

        if list[mid]==find:
            globals()['pos']=mid
            return True
        elif list[mid]<find:
            l=mid+1
        else:
            u=mid-1
    return False




size=int(input("Enter the size of list"))
print("Enter the elements of list")
list=[]
for i in range(size):
    list.append(int(input()))

find=int(input("Enter the number to be searched"))
list.sort()
print("sorted list is :",list)
if search(list,find):
    print("Found at ",pos)
else:
    print("Not found")