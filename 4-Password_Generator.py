import random
import string

def password_generator(length):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char) for _ in range(length))
    return f"Generated password: {password}"

length = int(input("enter the desired lenght of your password : "))
if length >= 4 and length <17:
    print(password_generator(length))
else:
    print("Password lenght should be between 4 to 16 characters")

