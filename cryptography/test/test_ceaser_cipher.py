from lib2to3.pgen2.tokenize import untokenize
from ceaser_cipher import encrypt
import unittest

class TestCeaserEncrypt(unittest.TestCase):
    def test(self):
        self.assertEqual(encrypt("chris",2),"ejtku")
if __name__ == "__main__":
    unittest.main()