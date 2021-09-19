import string
import random


def generate_unique_id():
    dictionary = ''
    dictionary += string.ascii_uppercase + string.ascii_lowercase + string.digits
    unique_id = ''.join(random.choices(dictionary, k = 24))
    return unique_id


if __name__ == "__main__":
    generate_unique_id()