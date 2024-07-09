import random
import string

def generate_password(length):
    # Define a string containing all possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use random.choices() to generate a list of random characters
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length must be greater than zero. Please try again.")
                continue
            
            password = generate_password(length)
            print("Generated password:", password)
            
            break  # Exit the loop after generating and displaying the password
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()