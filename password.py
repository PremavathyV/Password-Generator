import random
import string

def generate_password(length=12):
    # Define the characters that will be used to generate the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters from the list of available characters
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Example usage
password = generate_password(16)  # Password length set to 16 characters
print("Generated Password:", password)
