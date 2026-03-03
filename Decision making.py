age=int(input("Enter your Age : "))
if age<18:
    print("Minor")
elif age>18 & age<60:
    print("Major")
else:
    print("Aged")

a=int(input("Enter number : "))
if a>0:
      print("Positive")
else:
    print("Negative")
marks=int(input("enter your marks : "))
if marks>=90:
          print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("Fail")
age=int(input("Enetr your Age : "))
if(age>18):
    print("You are Allowed")
    if(age>60):
        print("lower Seat")
    else:
         print("Upper Seat")
else:
    print("Not Allowed")
   
#Ternary Operator

a = 10
b = 20
print("a is greater" if a > b else "b is greater")

