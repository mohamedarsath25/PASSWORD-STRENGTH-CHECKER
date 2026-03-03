n=10
for i in range(1,n+1):
    print(i,end=" ")
print()
n=10
for i in range(2,n+1,2):
    print(i,end=" ")
print()
n=10
for i in range(1,n+1,2):
    print(i,end=" ")
print()
for i in range(1,n+1):
    print(i*i,end=" ")
print()
for i in range(1,n+1):
    print(i*i*i,end=" ")
print()
#fibonacci series
n=10
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
print()
#prime number series
n=50
for num in range(2,n+1):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    if(count==2):
        print(num,end=" ")
print()
#Arithmetic progression
a=2
d=3
n=6
for i in range(n):
    print(a,end=" ")
    a=a+d
print()
#Geometric progression
a=2
r=3
n=6
for i in range(n):
    print(a,end=" ")
    a=a*r
print()
#factorial series
n=6
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact,end=" ")
print()
#Traingular Numbers
n=6
sum=0
for i in range(1,n+1):
    sum=sum+i
    print(sum,end=" ")
print()
#Power of 2 series
n=6
for i in range(1,n+1):
    print(2**i,end=" ")
print()
#Alternate + and - series
n=10
for i in range(1,n+1):
    if(i%2==0):
        print(-i,end=" ")
    else:
        print(i,end=" ")
print()
#Mixed Pattern
n=10
for i in range(1,n+1):
    print(i*(i+1),end=" ")
print()
#reverse natural number
n=10
for i in range(n,0,-1):
    print(i,end=" ")
print()
#Armstrong Number
for num in range(1,1000):
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp//=10
    if(sum==num):
        print(num,end=" ")
#Palindrome Series

    
    
