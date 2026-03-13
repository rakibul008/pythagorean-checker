def login_system():
    print("--- Welcome to the System ---")

    attempts = 0

    while attempts < 3:
        username = input("Enter a 6-letter username: ")
        password = input("Enter your password: ")

        valid_user = len(username) == 6 and username.isalpha()
        valid_pass = "SWUSTCST" in password

        if valid_user and valid_pass:
            print("\nLogin successful!")
            return True
        else:
            print("Error: Invalid username or password. Try again.\n")

        attempts += 1

    print("Maximum attempts reached. System locked.")
    return False


def check_pythagorean():
    print("\n--- Pythagorean Checker ---")

    while True:
        print("\nPlease enter three positive whole numbers.")
        try:
            a = int(input("First number (a): "))
            b = int(input("Second number (b): "))
            c = int(input("Third number (c): "))

            if a <= 0 or b <= 0 or c <= 0:
                print("Error: All numbers must be greater than zero. Try again.\n")
                continue

            a_sq = a ** 2
            b_sq = b ** 2
            c_sq = c ** 2

            if c >= a and c >= b:
                form = "a\u00B2 + b\u00B2 = c\u00B2"
                step1 = f"{a}\u00B2 + {b}\u00B2 = {c}\u00B2"
                step2 = f"{a_sq} + {b_sq} = {c_sq}"
                sum_val = a_sq + b_sq
                target_val = c_sq
            elif b >= a and b >= c:
                form = "a\u00B2 + c\u00B2 = b\u00B2"
                step1 = f"{a}\u00B2 + {c}\u00B2 = {b}\u00B2"
                step2 = f"{a_sq} + {c_sq} = {b_sq}"
                sum_val = a_sq + c_sq
                target_val = b_sq
            else:
                form = "b\u00B2 + c\u00B2 = a\u00B2"
                step1 = f"{b}\u00B2 + {c}\u00B2 = {a}\u00B2"
                step2 = f"{b_sq} + {c_sq} = {a_sq}"
                sum_val = b_sq + c_sq
                target_val = a_sq

            print("\n--- Calculating ---")
            print(form)
            print(step1)
            print(step2)
            print(f"{sum_val} = {target_val}")

            if sum_val == target_val:
                print(f"\nResult: YES! {a}, {b}, and {c} are Pythagorean.")
            else:
                print(f"\nResult: NO. {a}, {b}, and {c} are NOT Pythagorean.")

            choice = input(
                "\nDo you want to check another set? (type 'yes' to try again, or 'exit' to logout): ").strip().lower()

            if choice == 'exit' or choice == 'logout':
                print("Logging out... Have a great day!")
                break

        except ValueError:
            print("Error: Invalid input! Please enter numbers only.\n")


if __name__ == "__main__":
    if login_system():
        check_pythagorean()