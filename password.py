import random
import string
def generate_password(length):
    """
    Generate a password of the given length.
    Args:
        length (int): The length of the password.
    Returns:
        str: The generated password.
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
def main():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length < 8:
                print("Password length should be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    password = generate_password(length)
    print("Generated Password : ", password)
if __name__ == "__main__":
    main()
