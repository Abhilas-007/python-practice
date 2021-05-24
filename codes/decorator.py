
def div(a,b):
    print(a/b)

#decorator-it changes the logic of other func to make it appropieate to us
def smrt_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div1=smrt_div(div)
div1(2,4)