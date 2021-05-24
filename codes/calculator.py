x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print("Enter operation")
print("1.+\n2.-\n3.*\n4./")
op=int(input())
result=0
if(op==1):
    result=x+y
elif(op==2):
    result=x-y
elif(op==3):
    result=x*y
elif(op==4):
    result=x/y
else:
    print("Choice was not valid")
print(f"Result is: ",result)
