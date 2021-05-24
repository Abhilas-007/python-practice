num=int(input("Enter a number to check prime "))
for i in range(2,(num//2)+1):
    if num % i==0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
#Here is an example of for-else here the else block is executed only if the break in for loop is executed otherwise not