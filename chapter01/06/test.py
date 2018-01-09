import unittest

from code import n_gram

class CodeTest(unittest.TestCase):
    def test_union(self):
        X = set(n_gram('paraparaparadise', 2))
        Y = set(n_gram('paragraph', 2))

        actual = set.union(X, Y)
        self.assertEqual(set(['pa', 'ag', 'is', 'ar', 'ap', 'se', 'di', 'gr', 'ra', 'ph', 'ad']), actual)

    def test_intersection(self):
        X = set(n_gram('paraparaparadise', 2))
        Y = set(n_gram('paragraph', 2))

        actual = set.intersection(X, Y)
        self.assertEqual(set(['pa', 'ar', 'ra', 'ap']), actual)

    def test_difference(self):
        X = set(n_gram('paraparaparadise', 2))
        Y = set(n_gram('paragraph', 2))

        actual = X.difference(Y)
        self.assertEqual(set(['ad', 'se', 'is', 'di']), actual)

    def test_is_included(self):
        X = set(n_gram('paraparaparadise', 2))
        Y = set(n_gram('paragraph', 2))

        actual_with_x = 'se' in X
        actual_with_y = 'se' in Y
        self.assertTrue(actual_with_x)
        self.assertFalse(actual_with_y)

if __name__ == '__main__':
    unittest.main()
