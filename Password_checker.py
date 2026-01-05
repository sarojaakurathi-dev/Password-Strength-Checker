import string
import getpass


def analyze_password(password):
    """Analyze password and return character counts"""
    counts = {
        "lower": 0,
        "upper": 0,
        "digit": 0,
        "space": 0,
        "special": 0
    }

    for char in password:
        if char.islower():
            counts["lower"] += 1
        elif char.isupper():
            counts["upper"] += 1
        elif char.isdigit():
            counts["digit"] += 1
        elif char.isspace():
            counts["space"] += 1
        else:
            counts["special"] += 1

    return counts


def calculate_strength(counts):
    """Calculate password strength score"""
    strength = sum(1 for value in counts.values() if value > 0)
    return strength


def get_remarks(strength):
    """Return remarks based on strength"""
    remarks = {
        1: "Very weak password. Change it immediately.",
        2: "Weak password. Consider improving it.",
        3: "Average password. Can be stronger.",
        4: "Strong password. Hard to guess.",
        5: "Very strong password. Excellent security!"
    }
    return remarks.get(strength, "Invalid password")


def display_result(counts, strength):
    """Display password analysis result"""
    print("\nPassword Analysis:")
    print(f"Lowercase letters : {counts['lower']}")
    print(f"Uppercase letters : {counts['upper']}")
    print(f"Digits            : {counts['digit']}")
    print(f"Whitespaces       : {counts['space']}")
    print(f"Special characters: {counts['special']}")
    print(f"Strength Score    : {strength}/5")
    print(f"Remarks           : {get_remarks(strength)}")


def check_password():
    """Main password check function"""
    password = getpass.getpass("Enter your password: ")
    counts = analyze_password(password)
    strength = calculate_strength(counts)
    display_result(counts, strength)


def main():
    print("===== Password Strength Checker =====")

    while True:
        choice = input("\nDo you want to check a password? (y/n): ").lower()
        if choice == 'y':
            check_password()
        elif choice == 'n':
            print("Thank you for using the Password Strength Checker.")
            break
        else:
            print("Invalid input! Please enter y or n.")


if __name__ == "__main__":
    main()
