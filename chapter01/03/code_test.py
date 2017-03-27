import unittest

from code import char_count


class CodeTest(unittest.TestCase):
    def test_char_count(self):
        target = 'Now I need a drink, alcoholic of course, ' \
                 'after the heavy lectures involving quantum mechanics.'
        expected = [
            ('Now', 3),
            ('I', 1),
            ('need', 4),
            ('a', 1),
            ('drink,', 6),
            ('alcoholic', 9),
            ('of', 2),
            ('course,', 7),
            ('after', 5),
            ('the', 3),
            ('heavy', 5),
            ('lectures', 8),
            ('involving', 9),
            ('quantum', 7),
            ('mechanics.', 10)
        ]
        self.assertEqual(expected, char_count(target))


if __name__ == '__main__':
    unittest.main()
