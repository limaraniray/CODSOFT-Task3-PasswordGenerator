"""
CODSOFT Python Internship - Task 3
Password Generator Application
"""

import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase  # always include lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    # Guarantee at least one char from each selected category
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    password.append(random.choice(string.ascii_lowercase))

    # Fill remaining length
    remaining = length - len(password)
    password += random.choices(characters, k=remaining)

    random.shuffle(password)
    return "".join(password)

def password_strength(length, use_upper, use_digits, use_symbols):
    score = 0
    if length >= 8:  score += 1
    if length >= 12: score += 1
    if length >= 16: score += 1
    if use_upper:    score += 1
    if use_digits:   score += 1
    if use_symbols:  score += 1

    if score <= 2:   return "🔴 Weak"
    elif score <= 4: return "🟡 Moderate"
    else:            return "🟢 Strong"

def get_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "yes"):
            return True
        elif ans in ("n", "no"):
            return False
        print("❌ Please enter 'y' or 'n'.")

def main():
    print("\n" + "="*45)
    print("       🔐 PASSWORD GENERATOR APP")
    print("="*45)

    while True:
        # Get password length
        while True:
            try:
                length = int(input("Enter desired password length (4-64): "))
                if 4 <= length <= 64:
                    break
                print("❌ Please enter a length between 4 and 64.")
            except ValueError:
                print("❌ Invalid input. Enter a number.")

        # Complexity options
        print("\nCustomize your password:")
        use_upper   = get_yes_no("Include uppercase letters? (y/n): ")
        use_digits  = get_yes_no("Include digits (0-9)?        (y/n): ")
        use_symbols = get_yes_no("Include symbols (!@#...)?    (y/n): ")

        # Generate password
        how_many = 1
        try:
            how_many = int(input("How many passwords to generate? (1-10): "))
            how_many = max(1, min(10, how_many))
        except ValueError:
            how_many = 1

        print("\n" + "-"*45)
        print(f"  Generated Password(s):")
        print("-"*45)
        for i in range(how_many):
            pwd = generate_password(length, use_upper, use_digits, use_symbols)
            strength = password_strength(length, use_upper, use_digits, use_symbols)
            print(f"  {i+1}. {pwd}   [{strength}]")
        print("-"*45)

        again = input("\nGenerate more passwords? (y/n): ").strip().lower()
        if again != "y":
            print("👋 Goodbye! Keep your passwords safe!")
            break

if __name__ == "__main__":
    main()
