
from reverse_decrypt import reverse_decrypt
import unittest

class TestDecrypt(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_decrypt("sirhc"),"chris")

if __name__ == "__main__":
    unittest.main()

