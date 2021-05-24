def fact(num,res):


    result =res*num
    if num>1:
        fact(num-1,result)
    else:
        print(result)




def fact2(num):
    if(num==0):
        return 1
    return num*fact2(num-1)

fact(int(input("Enter a number"
               " to find its factorial")),1)
res=fact2(int(input("Enter a number"
               " to find its factorial")))
print(res)