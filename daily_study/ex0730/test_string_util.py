# -*- coding : utf-8 -*-
import os
import unittest

import string_util

class UtilTestCase(unittest.TestCase):
    def setUp(self):
        print "setup"
        self.file_name = "temp_file.txt"
        with open(self.file_name, "w") as f:
            f.write("1 first line\n")
            f.write("2 second line\n")
            f.write("3 three line")

    def tearDown(self):
        print "tearDown"
        os.remove(self.file_name)

    def test_word_counter(self):
        self.assertEqual(
            string_util.word_counter(self.file_name),
            (9, 3)
            )

if __name__=="__main__":
    unittest.main(verbosity=2)
