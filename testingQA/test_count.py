import counting

def test_count_zeros():
    assert counting.count([0,0,0], 0) == 3

def test_count_string():
    assert counting.count(["a","a","a"], "a") == 3