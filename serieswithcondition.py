#NUMBER DIVISIBLE BY 2
n=10
for i in range(1,n+1):
    if(i%2==0):
       print(i,end=" ")
print()

#DIVISOR SUM SERIES
n=6
sum=0
print("Divisor:")
for i in range(1,n+1):
    if(n%i==0):
        sum=sum+i
       
        print(i,end=" ")
print()
print("Sum:",sum)
#Loop pattern
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()
#Trianglepattern
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print()
#PATTERN-RIGHT ALIGNED
n=4
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
