score=0
questions = [
("1.Who is Goat of Football ?",["A. Neymar","B. Ronaldo","C. Messi","D. Mohamed Arsath"],"B"),

("2.Cheif Minister of Tamilnadu?",["A. Thalapathy Vijay","B. M.K Stalin","C. Annamalai","D. Seeman"],"A"),

("3.Colour of Sky?",["A. Blue","B. White","C. Yellow","D. Orange"],"A"),

("4. 15 * 4 = ?",["A. 45","B. 50","C. 60","D. 65"],"C"),

("5.HTML stands for ?",["A. Hyper Text Markup Language","B. High Text Machine Language","C. Hyper Transfer Markup Language","D. Home Tool Markup Language"],"A"),

("6.Which OOP concept hides data?",["A. Inheritance","B. Polymorphism","C. Encapsulation","D. Abstraction"],"C"),

("7.Which keyword is used to define a function in Python?",["A. function","B. def","C. fun","D. define"],"B"),

("8.Which data type is used to store multiple items in one variable?",["A. int","B. string","C. list","D. float"],"C"),

("9.Which symbol is used for comments in Python?",["A. //","B. #","C. /* */","D. --"],"B"),

("10.What is the output of print(2**3)?",["A. 6","B. 8","C. 9","D. 5"],"B")
]

for q,options,ans in questions:
    print("\n"+q)
    for opt in options:
        print(opt)
    user = input("Enter your answer (A/B/C/D): ").upper()
    if(user==ans):
         print("Correct Answer")
         score=score+1
    else:
          print("Wrong Answer")
print("Quiz Completed")
print("Score: ",score,"/",len(questions)) 

    
   
    

