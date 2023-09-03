import random
import string

def generate_random_number():
    return random.randint(1, 1000000)

def generate_random_string(length):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


random_string = generate_random_string(10)
print(random_string)


random_number = generate_random_number()
print(random_number)