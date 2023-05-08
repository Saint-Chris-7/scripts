from lib2to3.pgen2.tokenize import untokenize
import unittest
from verman_cipher import encrypt

class TestVermanEncrypt(unittest.TestCase):
    def test(self):
        self.assertEqual(encrypt("chris","abcde"),"ÄÊÕÍØ")

if __name__ == "__main__":
    unittest.main()