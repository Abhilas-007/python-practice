x=int(input("Enter a number"))
for i in range(0,x+1):
    for k in range(x-i):
        print(" ",end="")
    for j in range(i):
        print("#",end=" ")
    print()