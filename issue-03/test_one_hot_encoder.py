from one_hot_encoder import fit_transform
import unittest


class TestOneHotEncoder(unittest.TestCase):
    def test_cities_list(self):
        """This test - cities from the work example"""
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(cities)
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_cities_strs(self):
        """This test - increased the number of cities"""
        actual = fit_transform('Moscow', 'New York', 'Moscow', 'London',
                               'Moscow', 'Moscow', 'Smolensk', 'Smolensk')
        expected = [
            ('Moscow', [0, 0, 0, 1]),
            ('New York', [0, 0, 1, 0]),
            ('Moscow', [0, 0, 0, 1]),
            ('London', [0, 1, 0, 0]),
            ('Moscow', [0, 0, 0, 1]),
            ('Moscow', [0, 0, 0, 1]),
            ('Smolensk', [1, 0, 0, 0]),
            ('Smolensk', [1, 0, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_type_error_args(self):
        """This test shows, that not str objects can be one hot encoded only
        contained in the list, not passed as args*"""
        self.assertRaises(TypeError, fit_transform, 1, 2, 3, 2, 1)

    def test_type_error_len(self):
        """This test checks if TypeError raises if there is nothing passed
        as argument in function"""
        with self.assertRaises(TypeError) as e:
            fit_transform()
        self.assertIn('expected at least 1 arguments, got 0', str(e.exception))

    def test_several_iterable(self):
        """This test shows that only the first iterable object passed in the
        function will be transformed"""
        actual = fit_transform([0], [1], [2], [1], [0])
        expected = [
            ([0], [0, 0, 1]),
            ([1], [0, 1, 0]),
            ([2], [1, 0, 0]),
            ([1], [0, 1, 0]),
            ([0], [0, 0, 1]),
        ]
        self.assertNotEqual(actual, expected)

    def test_different_types(self):
        """This test shows that types can be different, 1.0 and 1 - the
        same objects"""
        actual = fit_transform(('chunk', 1, 1, 2, False, 1.0))
        expected = [
            ('chunk', [0, 0, 0, 1]),
            (1, [0, 0, 1, 0]),
            (1, [0, 0, 1, 0]),
            (2, [0, 1, 0, 0]),
            (False, [1, 0, 0, 0]),
            (1.0, [0, 0, 1, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_mutable_type(self):
        """This test shows that mutable type can't be processed
        by function"""
        with self.assertRaises(TypeError) as e:
            fit_transform([[1], [2], [1]])
        self.assertTrue("unhashable type: 'list'" == str(e.exception))
