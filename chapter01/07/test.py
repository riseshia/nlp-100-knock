import unittest

from code import formatter

class CodeTest(unittest.TestCase):
    def test_formatter(self):
        actual = formatter('x', 'y', 'z')
        self.assertEqual('x時のyはz', actual)


if __name__ == '__main__':
    unittest.main()
