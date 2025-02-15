from twttr import shorten

def test_string():
    assert shorten("mArco") == "mrc"

def test_num():
    assert shorten("1") == "1"

def test_pont():
    assert shorten(".") == "."

