score = 0

print("Welcome to the Python MCQ Quiz")
print("Answer by typing A, B, C, or D\n")

print("1. What is the output of print(type(10))?")
print("A) int\nB) float\nC) str\nD) bool")
ans = input("Your answer: ").upper()
if ans == "A":
    score += 1

print("\n2. Which symbol is used for comments in Python?")
print("A) //\nB) #\nC) /* */\nD) --")
ans = input("Your answer: ").upper()
if ans == "B":
    score += 1

print("\n3. What is the output of print(3 * \"Hi\")?")
print("A) HiHiHi\nB) 9\nC) Error\nD) Hi*3")
ans = input("Your answer: ").upper()
if ans == "A":
    score += 1

print("\n4. Which data type is immutable?")
print("A) List\nB) Dictionary\nC) Set\nD) Tuple")
ans = input("Your answer: ").upper()
if ans == "D":
    score += 1

print("\n5. What is the output of len([1, 2, 3, 4])?")
print("A) 3\nB) 4\nC) 5\nD) Error")
ans = input("Your answer: ").upper()
if ans == "B":
    score += 1

print("\n6. Which keyword is used to define a function in Python?")
print("A) function\nB) fun\nC) def\nD) define")
ans = input("Your answer: ").upper()
if ans == "C":
    score += 1

print("\n7. What will print(5 // 2) output?")
print("A) 2.5\nB) 3\nC) 2\nD) 2.0")
ans = input("Your answer: ").upper()
if ans == "C":
    score += 1

print("\n8. Which of the following is used to store key-value pairs?")
print("A) List\nB) Tuple\nC) Set\nD) Dictionary")
ans = input("Your answer: ").upper()
if ans == "D":
    score += 1

print("\n9. What is the output of print(bool(\"\"))?")
print("A) True\nB) False\nC) None\nD) Error")
ans = input("Your answer: ").upper()
if ans == "B":
    score += 1

print("\n10. Which loop is used when the number of iterations is unknown?")
print("A) for\nB) while\nC) do-while\nD) foreach")
ans = input("Your answer: ").upper()
if ans == "B":
    score += 1

print("\n11. Which function is used to take input from user?")
print("A) read()\nB) scan()\nC) input()\nD) get()")
ans = input("Your answer: ").upper()
if ans == "C":
    score += 1

print("\n12. What is the output of print(10 % 3)?")
print("A) 1\nB) 3\nC) 0\nD) 10")
ans = input("Your answer: ").upper()
if ans == "A":
    score += 1

print("\n13. Which operator is used for exponentiation?")
print("A) ^\nB) **\nC) //\nD) %")
ans = input("Your answer: ").upper()
if ans == "B":
    score += 1

print("\n14. What is the output of print(len(\"Python\"))?")
print("A) 5\nB) 6\nC) 7\nD) Error")
ans = input("Your answer: ").upper()
if ans == "B":
    score += 1

print("\n15. Which data type stores multiple values in order?")
print("A) list\nB) set\nC) float\nD) bool")
ans = input("Your answer: ").upper()
if ans == "A":
    score += 1

print("\n16. Which keyword is used to exit a loop?")
print("A) stop\nB) exit\nC) break\nD) return")
ans = input("Your answer: ").upper()
if ans == "C":
    score += 1

print("\n17. What is the output of print(2 == 2)?")
print("A) True\nB) False\nC) 2\nD) Error")
ans = input("Your answer: ").upper()
if ans == "A":
    score += 1

print("\n18. Which of the following is a Boolean value?")
print("A) yes\nB) 1\nC) True\nD) on")
ans = input("Your answer: ").upper()
if ans == "C":
    score += 1

print("\n19. Which keyword is used for decision making?")
print("A) for\nB) if\nC) while\nD) switch")
ans = input("Your answer: ").upper()
if ans == "B":
    score += 1

print("\n20. What is the output of print(type([]))?")
print("A) <class 'list'>\nB) tuple\nC) set\nD) dictionary")
ans = input("Your answer: ").upper()
if ans == "A":
    score += 1

print("\nQuiz Completed")
print("Total Correct Answers:", score, "out of 20")
