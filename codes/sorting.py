
def bbleSrt(list):

    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp


def selSrt(list):

    for i in range(len(list)):
        minpo=i
        for j in range(i,len(list)):
            if list[j]<list[minpo]:
                minpo=j
        temp = list[i]
        list[i] = list[minpo]
        list[minpo] = temp




list=[3,55,2,747,1,45,32,78]

selSrt(list)

print(list)