import unittest

from code import n_gram

class CodeTest(unittest.TestCase):
    def test_char_1_gram(self):
        target = 'I am an NLPer'
        actual = n_gram(target, 1)
        self.assertEqual(['I', ' ', 'a', 'm', ' ', 'a', 'n', ' ', 'N', 'L', 'P', 'e', 'r'], actual)

    def test_char_2_gram(self):
        target = 'I am an NLPer'
        actual = n_gram(target, 2)
        self.assertEqual(['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er'], actual)

    def test_word_1_gram(self):
        target = 'I am an NLPer'
        actual = n_gram(target.split(' '), 1)
        self.assertEqual(['I', 'am', 'an', 'NLPer'], actual)

    def test_word_2_gram(self):
        target = 'I am an NLPer'
        actual = n_gram(target.split(' '), 2, tokenizer=' ')
        self.assertEqual(['I am', 'am an', 'an NLPer'], actual)

if __name__ == '__main__':
    unittest.main()
