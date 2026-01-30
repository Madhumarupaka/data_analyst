# l1=[1,3,4,5,7] l2=[4,5,6,8,4]  target=8


def fun(l1,l2,target):

    for x in range(len(l1)):
        for y in range(len(l2)):
            if l1[x]+l2[y]==target:
                print([x,y],end=" ")


l1=[1,3,4,5,7]
l2=[4,5,6,8,4]
target=8
fun(l1,l2,target)


