import unittest

from code import typoglycemia

class CodeTest(unittest.TestCase):
    def test_typoglycemia_do_not_shuffle(self):
        actual = typoglycemia('shia')
        self.assertEqual('shia', actual)

    def test_typoglycemia_do_shuffle(self):
        actual = typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
        expected = "Iut urt   chnInte doitl o eahlwb adpi tn  ahnawmnmlunoaeoelpeatvee mec' iI :ou ea sd r thgcnlfl aues yhwrdtdahdn."
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
