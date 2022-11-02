from one_hot_encoder import fit_transform
import pytest


def test_cities_list():
    """This test - cities from the work example"""
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = fit_transform(cities)
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_cities_strs():
    """This test - increased the number of cities"""
    actual = fit_transform('Moscow', 'New York', 'Moscow', 'Praga',
                           'Moscow', 'Moscow', 'Smolensk', 'Praga')
    expected = [
        ('Moscow', [0, 0, 0, 1]),
        ('New York', [0, 0, 1, 0]),
        ('Moscow', [0, 0, 0, 1]),
        ('Praga', [0, 1, 0, 0]),
        ('Moscow', [0, 0, 0, 1]),
        ('Moscow', [0, 0, 0, 1]),
        ('Smolensk', [1, 0, 0, 0]),
        ('Praga', [0, 1, 0, 0]),
    ]
    assert actual == expected


def test_type_error_args():
    """This test shows, that not str objects can be one hot encoded only
    contained in the list, not passed as args*"""
    with pytest.raises(TypeError):
        fit_transform(1, 0, -1, 0, 1)


def test_type_error_len():
    """This test checks if TypeError raises if there is nothing passed
    as argument in function"""
    with pytest.raises(TypeError) as e:
        fit_transform()
    assert 'expected at least 1 arguments, got 0' in str(e)


def test_several_iterable():
    """This test shows that only the first iterable object passed in the
    function will be transformed"""
    actual = fit_transform([102], [10], [2], [10], [102])
    expected = [
        ([102], [0, 0, 1]),
        ([10], [0, 1, 0]),
        ([2], [1, 0, 0]),
        ([10], [0, 1, 0]),
        ([102], [0, 0, 1]),
    ]
    assert actual != expected


def test_different_types():
    """This test shows that types can be different, 5.0 and 5 - the
    same objects"""
    actual = fit_transform(('batch', 5.0, 5, 202, True, 5.0))
    expected = [
        ('batch', [0, 0, 0, 1]),
        (5.0, [0, 0, 1, 0]),
        (5, [0, 0, 1, 0]),
        (202, [0, 1, 0, 0]),
        (True, [1, 0, 0, 0]),
        (5.0, [0, 0, 1, 0]),
    ]
    assert actual == expected


def test_mutable_type():
    """This test shows that mutable type can't be processed
    by function"""
    with pytest.raises(TypeError) as e:
        fit_transform([['c'], ['a'], ['c']])
    assert "unhashable type: 'list'" in str(e)
