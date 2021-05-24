
def fibo(n):
    a=0
    b=1
    c=0
    if n==0:
        print("Enter a valid number")
    elif n==1:
        print(a)
    elif n<0:
        print("Enter a positive number")
    else:
        print(a)
        print(b)

        while c < n:
            c = a + b
            a = b
            b = c
            if c<=n:
                print(c)


fibo(int(input("Enter a number: ")))