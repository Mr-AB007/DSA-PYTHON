import random
import string


def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_specials):

    uppercase_list= string.ascii_uppercase
    lowercase_list =  string.ascii_lowercase
    number_list = string.digits
    special_list = string.punctuation

    password_chars = []
    if use_uppercase:
        password_chars.append(random.choice(uppercase_list))
    if use_lowercase:
        password_chars.append(random.choice(lowercase_list))
    if use_numbers:
        password_chars.append(random.choice(number_list))
    if use_specials:
        password_chars.append(random.choice(special_list))

    # Fill the rest
    all_selected = []
    if use_uppercase:
        all_selected += uppercase_list
    if use_lowercase:
        all_selected += lowercase_list
    if use_numbers:
        all_selected += number_list
    if use_specials:
        all_selected += special_list

    remaining_length = length - len(password_chars)
    password_chars += [random.choice(all_selected) for _ in range(remaining_length)]
    random.shuffle(password_chars)

    return ''.join(password_chars)


def get_user_input():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_specials = input("Include special characters? (y/n): ").lower() == 'y'

    return length, use_uppercase, use_lowercase, use_numbers, use_specials


def main():
    print("Welcome to the Password Generator!")

    while True:
        user_input = get_user_input()
        if user_input is None:
            continue

        length, use_uppercase, use_lowercase, use_numbers, use_specials = user_input

        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_specials)
        print("\nGenerated Password:", password)

        another = input("\nGenerate another password? (y/n): ").lower()
        if another != 'y':
            print("Thank you for using the Password Generator!")
            break


if __name__ == "__main__":
    main()
