# User Guessing Game (Computer Feedback Based)

# Step 1: Start request
start = input("Do you want to start the game? (yes/no): ").lower()
if start != "yes":
    print("Game exited.")
    exit()

# Step 2: Rules using tuple
rules = (
    "Computer will think of a number between 1 and 100",
    "You have to guess the number",
    "Computer will reply with: Too Low, Too High, or Correct"
)

print("\nGame Rules:")
for rule in rules:
    print("-", rule)

input("\nPress Enter to start the game...")

# Step 3: Import and data structures
import random

secret_number = random.randint(1, 100)

guess_list = []   # list to store guesses
attempts = 0

# Step 4: Guessing loop
while True:

    user_guess = int(input("\nEnter your guess: "))

    attempts += 1
    guess_list.append(user_guess)

    if user_guess < secret_number:
        print("📉 Too Low")
    elif user_guess > secret_number:
        print("📈 Too High")
    else:
        print("\n🏆 YOU WON! Your guess is correct.")
        break


# Step 5: Store result using dictionary
game_result = {
    "Secret Number": secret_number,
    "Total Attempts": attempts,
    "Your Guesses": guess_list
}

# Step 6: Final result
print("\n--- Game Summary ---")

for key, value in game_result.items():
    print(key, ":", value)