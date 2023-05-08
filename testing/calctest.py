import unittest
from unittest import TestCase
from testing.calc import add

class CalcTest(TestCase):

    def test(self):
        added = add(9,9)
        self.assertEqual(added,18)
if __name__ == "__main__":
    unittest.main()
        