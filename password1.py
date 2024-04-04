import string
import secrets

def generate_password(length, num_special, num_numbers, num_upper):
    """Generate a random password of the specified length."""
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if num_upper > 0 else ''
    numbers = string.digits if num_numbers > 0 else ''
    special_characters = string.punctuation if num_special > 0 else ''

    all_characters = lowercase_letters + uppercase_letters + numbers + special_characters

    if length < num_special + num_numbers + num_upper:
        print("Warning: Password length should be greater than or equal to the sum of special characters, numbers, and uppercase letters.")

    password = ''.join(secrets.choice(all_characters) for i in range(length))
    return password

# Prompt the user to specify the desired length of the password
password_length = int(input("Enter the desired length of the password: "))

# Prompt the user to specify the number of special characters, numbers, and uppercase letters
num_special = int(input("Enter the number of special characters: "))
num_numbers = int(input("Enter the number of numbers: "))
num_upper = int(input("Enter the number of uppercase letters: "))

# Generate the password
generated_password = generate_password(password_length, num_special, num_numbers, num_upper)

# Display the generated password
print(f"Generated password: {generated_password}")