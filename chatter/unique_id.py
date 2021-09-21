import string
import random


def generate_unique_id():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    dictionary = ''.join((upper, lower, digits))
    unique_id = ''.join(random.choices(dictionary, k=24))
    return unique_id
