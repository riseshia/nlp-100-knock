import unittest

from code import merge_str


class CodeTest(unittest.TestCase):
    def test_merge_str(self):
        self.assertEqual('パタトクカシーー',
                         merge_str('パトカー', 'タクシー'))


if __name__ == '__main__':
    unittest.main()
