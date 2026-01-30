# n = int(input())
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
# if c==2:
#     print("prime")
# else:
#     print("not a prime")
#     # Time complexity is o(n)


# prime number using while loop

# def prime(n):
#     i=1
#     c=0
#     while i<=n:
#         if n%i==0:
#             c+=1
#         i+=1
#     if c==2:
#         print("prime")
#     else:
#         print("not a prime")
#
# n =int(input())
# prime(n)

n =int(input())
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print("not a prime")
        break
else:
    print("prime")
