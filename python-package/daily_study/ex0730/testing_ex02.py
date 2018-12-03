# -*- coding: utf-8 -*-
import unittest
import calc

class TextCalcCase(unittest, TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
        self.assertEqual(calc.add(3, 5), 8)

    def test_sub(self):
        self.assertEqual(calc.add(1, 5), 7)
        self.assertEqual(calc.add(3, 5), 4)

if __name__=="__main__":
    unittest.main(verbosity=2)
