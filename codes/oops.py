#init method
class Laptop:
    def __init__(self):
        self.ram=16
        self.name='Lappy'
l1= Laptop()

print(l1.ram)
#here __init(self) method is constructor to class laptop like in java


#Inheritance

class Dad:
    def __init__(self):
        print("in Dad class init")

class Mom:
    def __init__(self):
        print("in Mom class init")
class Son(Dad):#-----------By this we can inherit the Dad class
    def __init__(self):
        super().__init__()#By this we can call the init method of the Dad class
        print("In Son class init")
class Daughter(Dad,Mom):#python allows multiple inheritance and the order of the printing init goes from left to right
    def __init__(self):
        super().__init__()#thats why here Dad init is printed called Method resolution order(MOR)
        print("in Daughter class init")
s=Son()#if in Son class init method is not present then it will go to the super class Dad
print()
d=Daughter()



#Polymorphism
##1.Duck typing
##2.Operator overloading
##3.Method overloading and method overriding

##Duck typing
print()
print("Polymorphism: Ducktyping-------------------------------------------")
class Computer:

    def code(self,ide):
        print("compile")
        print("Run")
        ide.process()

class PyCharm:

    def process(self):
        print("Executing in pycharm")

class MyEditor:

    def process(self):
        print("Executing in myeditor")


#Hrer pycharm and myeditor can be passed as an argument in code of computer so
#Both pycharm and myeditor act and beheave like same and called duck typing
py=PyCharm()
m=MyEditor()
c=Computer()
c.code(py)
c.code(m)


##Operator overloading
print()
print("Polymorphism: Operator overloading-------------------------------------------------------")

a=8
b=4
c=a+b#internally it will execute int.__add__(a,b)
print(c)
print(int.__add__(a,b))

class Student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1=self.m1+other.m2
        m2=self.m1+other.m2
        s3=Student(m1,m2)
        return s3

    def __gt__(self, other):#gt-greateer than(Comparing)
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2

        if m1>m2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {} '.format(self.m1,self.m2)#these curly brackets replaced by the 2 values and string is returned
s1=Student(70,80)
s2=Student(90,80)

s3=s1+s2 #internally '+' call __add__() and then our defined method gets executed

print(s3.m2)

if(s1>s2):#internally call __gt__() method to compare
    print("S1 wins")
else:
    print("S2 wins")

print(s1)#this __str_-() method is like a toString methos in java and we override it in above student class

##Method overloading

#method overloading is not there in python we make it in different way

# overloading is same name diff parameter

class Foo:

    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
           s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a

        return s

e=Foo()
print(e.sum(1))
print(e.sum(2,2))
print(e.sum(2,2,3))
#same method different argument

###Overriding
class A:
    def show(self):
        print("In A")
class B:
    def show(self):
        print("In B")
b=B()
b.show()


#Abstract
#python by default doesnot support abstract class

from abc import ABC,abstractmethod#used to define abstract class

class X(ABC):
    @abstractmethod
    def run(self):
        pass
class Y(X):
    def run(self):
        print("overidden method of abstract class")

y=Y()
y.run()