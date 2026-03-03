# Password Strength Checker using Python

rules = (
    "Minimum 6 characters",
    "At least one uppercase letter",
    "At least one lowercase letter",
    "At least one digit",
    "No spaces allowed"
)

print("Password Rules:")
for rule in rules:
    print("-", rule)

while True:

    password = input("\nEnter your password: ")

    password_chars = list(password)

    conditions = {
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "digit": False,
        "space": True
    }

    if len(password) >= 6:
        conditions["length"] = True

    for ch in password_chars:

        if ch.isupper():
            conditions["uppercase"] = True

        elif ch.islower():
            conditions["lowercase"] = True

        elif ch.isdigit():
            conditions["digit"] = True

        elif ch == " ":
            conditions["space"] = False


    score = 0

    for key, value in conditions.items():

        if key == "space":
            if value:
                score += 1
        else:
            if value:
                score += 1


    if score <= 2:
        strength = "WEAK"

    elif score <= 4:
        strength = "MEDIUM"

    else:
        strength = "STRONG"


    print("\nPassword Strength:", strength)


    if strength == "STRONG":

        print("Password accepted successfully!")
        break

    else:

        print("Please create a stronger password.")