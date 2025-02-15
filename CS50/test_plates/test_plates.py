from plates import is_valid

def test_startletters():
    assert is_valid("1AVSH") == False
    assert is_valid("ABCDE") == True

def test_minmax():
    assert is_valid ("ASDFVSASW") == False
    assert is_valid ("ABSTA") == True

def test_numbers():
    assert is_valid ("A23BS") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA022") == False
    assert is_valid ("20AAB") == False
    assert is_valid("A222") ==False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") ==False

def test_ponctuation():
    assert is_valid("AC.34") == False
    assert is_valid("AAAA!") == False
    assert is_valid("-ABC") == False

def test_zero():
    assert is_valid("AB01") == False
    assert is_valid ("ABC10") ==True
