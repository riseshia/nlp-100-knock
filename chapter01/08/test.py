import unittest

from code import encode, decode

class CodeTest(unittest.TestCase):
    def test_encode(self):
        actual = encode('shia1234')
        self.assertEqual('hsrz1234', actual)

    def test_decode(self):
        actual = decode('hsrz1234')
        self.assertEqual('shia1234', actual)

if __name__ == '__main__':
    unittest.main()
