from chatter import unique_id
import re


""" Tests if the returned unique_id
only has alphanumeric chars and if its exactly 24 chars long """


def test_unique_id():
    id = unique_id.generate_unique_id()
    regex = "^[a-zA-Z0-9]{24}$"
    assert re.match(regex, id)
