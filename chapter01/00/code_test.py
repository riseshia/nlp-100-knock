import unittest

from code import reverse


class CodeTest(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual('desserts',
                         reverse('stressed'))


if __name__ == '__main__':
    unittest.main()
