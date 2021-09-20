import string
import random


def generate_unique_id():
    letters = (string.ascii_uppercase, string.ascii_lowercase)
    digits = string.digits
    dictionary = ''.join((str(letters), digits))
    unique_id = ''.join(random.choices(dictionary, k=24))
    return unique_id
