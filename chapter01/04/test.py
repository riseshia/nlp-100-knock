import unittest

from code import element_dic


class CodeTest(unittest.TestCase):
    def test_dictionary(self):
        expected = [
            ('H', 1),
            ('He', 2),
            ('Li', 3),
            ('Be', 4),
            ('B', 5),
            ('C', 6),
            ('N', 7),
            ('O', 8),
            ('F', 9),
            ('Ne', 10),
            ('Na', 11),
            ('Mi', 12),
            ('Al', 13),
            ('Si', 14),
            ('P', 15),
            ('S', 16),
            ('Cl', 17),
            ('Ar', 18),
            ('K', 19),
            ('Ca', 20)
        ]
        dic = element_dic()
        for (key, order) in expected:
            self.assertEqual(order, dic[key])


if __name__ == '__main__':
    unittest.main()
