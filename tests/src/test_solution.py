import operator as op

import pytest
from src.solution import get_possible_partitions, get_possible_outputs


def test_get_possible_partitions_1():
    assert get_possible_partitions([7, 5, 5, 1]) == {
        ((7,), (1, 5, 5)),
        ((5,), (1, 5, 7)),
        ((1,), (5, 5, 7)),
        ((5, 7), (1, 5)),
        ((1, 7), (5, 5)),
        ((5, 5), (1, 7)),
        ((1, 5), (5, 7)),
    }


def test_get_possible_partitions_2():
    assert get_possible_partitions([2, 6, 7, 8, 9]) == {
        ((2,), (6, 7, 8, 9)),
        ((6,), (2, 7, 8, 9)),
        ((7,), (2, 6, 8, 9)),
        ((8,), (2, 6, 7, 9)),
        ((9,), (2, 6, 7, 8)),
        ((2, 6), (7, 8, 9)),
        ((2, 7), (6, 8, 9)),
        ((2, 8), (6, 7, 9)),
        ((2, 9), (6, 7, 8)),
        ((6, 7), (2, 8, 9)),
        ((6, 8), (2, 7, 9)),
        ((6, 9), (2, 7, 8)),
        ((7, 8), (2, 6, 9)),
        ((7, 9), (2, 6, 8)),
        ((8, 9), (2, 6, 7)),
    }


def test_get_possible_partitions_3():
    with pytest.raises(AssertionError):
        get_possible_partitions([7])


def test_get_possible_partitions_4():
    assert get_possible_partitions([8, 10]) == {((8,), (10,)), ((10,), (8,))}


def test_get_possible_partitions_5():
    assert get_possible_partitions([7, 7]) == {((7,), (7,))}


def test_get_possible_partitions_6():
    assert get_possible_partitions([7, 7, 2]) == {((7,), (2, 7)), ((2,), (7, 7))}


def test_get_possible_partitions_7():
    assert get_possible_partitions([1, 7, 2]) == {((7,), (1, 2)), ((1,), (2, 7)), ((2,), (1, 7))}


def test_get_possible_outputs_1():
    assert get_possible_outputs((7, 2)) == {14, 9, 5, -5}


def test_get_possible_outputs_2():
    assert get_possible_outputs((8, 4)) == {12, 32, 2, 4, -4}


def test_get_possible_outputs_3():
    assert get_possible_outputs((8, 0)) == {8, 0, -8}


def test_get_possible_outputs_4():
    assert get_possible_outputs((7, 2, 3)) == {
        12, 27, 3, 6, -6, 17, 42, 11, -11, 8, 15, 2, -2, -15, -8, 20, 5, 23, 19, -19, 35, 13, 1, -1, 7, -7
    }


def test_get_possible_outputs_5():
    assert 12 in get_possible_outputs((7, 5, 5, 1))


def test_get_possible_outputs_6():
    assert 12 in get_possible_outputs((3, 4, 7, 9))


def test_get_possible_outputs_7():
    assert 12 in get_possible_outputs((3, 5, 7, 9))


def test_get_possible_outputs_8():
    assert get_possible_outputs((4, 7, 9)) == {
        20, 99, 2, -2, 37, 19, -19, 12, 27, 3, 6, -6, -27, -3, -12, 64, 4, 67, 252, 59, -59, 91, 43, 29, -29, 35, -35, 8, -8
    }

# def test_generate_solutions_0():
#     solutions = generate_solutions([4, 3], 12)
#     assert solutions = ['4 * 3']


# def test_generate_solutions_1():
#     solutions = generate_solutions([7, 5, 5, 1], 12)
#     assert solutions == ['(7 - 5) * (5 + 1)']
