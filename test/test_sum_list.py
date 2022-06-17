from utility.sum_list import sum_list


# assert <boolean expression>
# assert is used to fail a test case IF the boolean expression is false

def test_sum_list_1():
    assert sum_list(10, 20) == 30


def test_sum_list_2():
    assert sum_list(10.1, 20.5) == 30.6


def test_sum_list_3():
    assert sum_list(10.1, -20) == -9.9


def test_sum_list_4():
    assert sum_list(2, 2, 2, 2) == 8


def test_sum_list_5():
    assert sum_list(2) == "Enter at least 2 numbers"

