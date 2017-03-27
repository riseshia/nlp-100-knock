import unittest

from code import pick_char


class CodeTest(unittest.TestCase):
    def test_pick_char(self):
        self.assertEqual('パトカー',
                         pick_char('パタトクカシーー'))


if __name__ == '__main__':
    unittest.main()
