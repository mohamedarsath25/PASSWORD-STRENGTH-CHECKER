**Password Strength Checker – Description**

This program is a Password Strength Checker that validates a user’s password based on predefined security rules. It ensures the password is strong before accepting it.

The program first displays the password rules, which are stored in a tuple. These rules include minimum length, presence of uppercase and lowercase letters, at least one digit, and no spaces.

It then uses a while True loop to repeatedly ask the user to enter a password until a strong password is provided.

A dictionary named conditions is used to track whether each rule is satisfied. The program checks:

If the password length is at least 6 characters.

If it contains at least one uppercase letter.

If it contains at least one lowercase letter.

If it contains at least one digit.

If it does not contain any spaces.

Each satisfied condition increases a score. Based on the score:

0–2 → WEAK

3–4 → MEDIUM

5 → STRONG

If the password is STRONG, it is accepted and the loop stops. Otherwise, the program asks the user to create a stronger password.
