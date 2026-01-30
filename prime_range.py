# find the prime numbers in given range
def prime( m , n ):
    count=0
    for i in range(m, n+1):
        if i>1:
            for x in range(2,i):
                if i%x==0:
                    break
            else:
                print(i)
                count+=1
    print("Count:",count)


m = int(input())
n = int(input())
prime(m,n)
# Time complexity is O(n**2)