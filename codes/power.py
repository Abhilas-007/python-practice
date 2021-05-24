x=int(input("Enter number: "))
y=int(input("Enter power: "))
result=1
while y>0:
    result*=x
    y-=1
print(result)