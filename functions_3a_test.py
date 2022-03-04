# 1, 3, 6 -> True
# 1, 10, 20 -> True
# 1, 1, 1 -> False
# 20, 10, 1 -> False
# 20, 10, 20 -> False
from functions_3a import is_ascending, word_concat


def test_is_ascending_good():
    assert is_ascending(1, 3, 6) == True


def test_is_ascending_same():
    assert is_ascending(1, 1, 1) == False  # ez ugyanaz, csak jobb -> assert not is_ascending(1, 1, 1)


def test_is_ascending_false():
    assert is_ascending(20, 10, 1) == False


def test_is_ascending_false2():
    assert is_ascending(20, 10, 20) == False

# "alma", "korte" -> "almakorte"
# "cseresznye", "meggy" -> "meggycseresznye"
# "korte", "meggy" -> kortemegy

def test_word_concat_1st_shorter():
    assert word_concat("alma", "korte") == "almakorte"


def test_word_concat_2nd_shorter():
    assert word_concat("korte", "alma") == "almakorte"

def test_word_concat_same():
    assert word_concat("korte", "meggy") == "kortemeggy"