'''num=int(input("Enter the number : "))
print("the number is even" if num%2==0 else "The number is add")
if(num%2==0):
    print("The number is even")
else:
    print("The number is odd")
A=int(input("Enrer the number : "))
B=int(input("Enrer the number : "))
C=int(input("Enrer the number : "))
if(A>B & A>C):
    print("A is greater")
elif(B>C & B>A):
    print("B is greater")
else:
    print("C is greater")
year=int(input("Enter the year"))
if (year%400==0 &(year%4==0 & year%100==0)):
    print("It is leap year")
else:
    print("it is  not leap year")
letter=input("Enter the Letter").lower()
if letter in 'aeiou':
    print("Vowel")
    
else:
    print("consonant")

a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
c=input("Enter the operator (+,-,*,/) : ")
if(c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="*"):
    print(a*b)
else:
    print(a/b)
 
'''
basic=float(input("Enter the salary"))
total=basic+(basic*0.2)+(basic*0.1)
print(total)
            
