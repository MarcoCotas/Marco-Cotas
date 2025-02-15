from bank import value


def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("hi") == 20

def test_else():
    assert value("marco") == 100
