# teszt eset == Python függvény
from functions_3rd_day import get_max


def test_get_max():
    #given: input adatok
    a=5
    b=10
    #when: ami a függvény eredménye
    result = get_max(a, b)
    #then
    assert result == 10


def test_get_max_when_first_value_is_greater():
    assert get_max(200, 5) == 200

def test_get_max_equal_values():
    assert get_max(100, 100) == 100

