

a=6
b=2

try:
    print(a/b)
    e=int(input("Enter a number "))
except ZeroDivisionError as e:
    print("Can not devide by zero: ",e)
except ValueError as e1:
    print("Enter correct value: ",e1)
except Exception as e2:
    print("Something went wrong: ",e2)
finally:
    print("Bye--------------")

#the exception handling is similar to java ,here the catch block is replaced by "except" block and the exceptions are different
#other than that all other things are similar to java