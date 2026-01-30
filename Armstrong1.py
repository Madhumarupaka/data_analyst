# check weather the number is armstrong or not
n = int(input())
temp=n
sum1=0
order=len(str(n))
while temp!=0:
    k=temp%10
    sum1+=k**order
    temp=temp//10
if n==sum1:
    print("Armstrong Number")
else:
    print("not a Armstrong Number")


