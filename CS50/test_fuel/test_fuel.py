from fuel import convert, gauge
import pytest

def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_xgreaty():
    with pytest.raises(ValueError):
        convert("5/2")

def test_validc():
    assert convert("2/4") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75

def test_e():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_f():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_validg():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
