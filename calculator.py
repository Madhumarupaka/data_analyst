def calculator(x,y,s):
    if s=="+":
        print(x+y)
    elif s=="-":
        print(x-y)
    elif s=="*":
        print(x*y)
    elif s=="%":
        print(x%y)


x=int(input())
y=int(input())
s=input()
calculator(x,y,s)
