from chatter import unique_id


def test_unique_id():
    assert len(unique_id.generate_unique_id()) == 24
