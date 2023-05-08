from ceaser_decrypt import ceaser_decrypt
import unittest

class TestDecyptCipher(unittest.TestCase):
    def test(self):
        self.assertEqual(ceaser_decrypt("ejtku",2),"chris")
        
if __name__ == "__main__":
    unittest.main()