from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)

t1=Hello()
t2=Hi()



t1.start()
sleep(0.2)#avoide collision between 2 threads
t2.start()

t1.join()#the main thread waits for the execution of thread t1 to finish
t2.join()#the main thread waits for the execution of thread t2 to finish

print("bye")