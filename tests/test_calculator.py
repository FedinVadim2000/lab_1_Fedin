from src import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_sub():
    assert calculator.sub(10, 5) == 5
