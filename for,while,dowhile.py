for num in range(0,10):
  print(num)
List1=[1,2,3,4,5]
for i in List1:
    print(i)
s=["a","b","c"]
for i in s:
    print(i)
for ch in "python":
    print("Character:",ch)
for i in range(1,50,2):
 print(i) 
for i in range(3):
    for j in range(2):
        print("i =",i, "j =",j)

a=int(input("Enter the table number:  "))
for i in range(1,11):
   print(i," * ",a," = ",i*a)

for i in range(5):
    if i==3:
        print("Skipping",i)
        continue
    if i==4:
        print("breaking at",i)
        break
    print("current",i)
       


numbers=[1,2,3,4,5,6]
eventotal=0
oddtotal=0
for num in numbers:
    if num%2==0:
        eventotal+=num
    if num%2!=0:
        oddtotal+=num
print("Eventotal",eventotal)
print("Oddtotal",oddtotal)

a=int(input("Enter the number you want count how much it divible  by 10 : "))
count=0
for i in range(1,a+1):
    if(i%10==0):
        count=count+1
print(count)

i=1
while i<=10:
    if i==6:
        break
    print(i)
    i+=1
i=1
while i<=10:
    if i==6:
        continue
    print(i)
    i+=1
i=1
while i<=10:
    if i==6:
        pass
    print(i)
    i+=1
    
for i in range(1,4):
    for j in range(1,4):
        print(i,j)

for i in range(3):
    for j in range(3):
        print("*",end=",")
    print()
