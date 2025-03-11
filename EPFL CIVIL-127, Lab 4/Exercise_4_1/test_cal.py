import unittest
from io import StringIO
import sys
from cal import Cal

class TestCal(unittest.TestCase):
    def test_january_2025(self):
        c = Cal()
        c.year(2025)
        c.month("jan")
        c.week_start("sun")
        output = StringIO()
        sys.stdout = output
        c.print()
        sys.stdout = sys.__stdout__
        expected_output = """    January 2025
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
"""
        self.assertEqual(output.getvalue(), expected_output)

    def test_august_2025(self):
        c = Cal()
        c.month("aug")
        c.year(2025)
        output = StringIO()
        sys.stdout = output
        c.print()
        sys.stdout = sys.__stdout__
        expected_output = """    August 2025
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
"""
        self.assertEqual(output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()