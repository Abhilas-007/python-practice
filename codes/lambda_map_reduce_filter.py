from functools import reduce
#def get_even(n):
    #return n%2==0
nums=[2,4,2,5,7,8,4,6]
print("The numbers are",nums)
#evens=list(filter(get_even,nums))# by use of external written function
evens=list(filter(lambda a : a%2 ==0,nums))#By the help of lamda expression#
print("The even numbers are",evens)

doubles=list(map(lambda a:a*2,evens))#us eof map and lamda function#

print("The doubles of all even number s are",doubles)

sum=reduce(lambda a,b:a+b,doubles)

print("The sum of doubles of even numbers is",sum)