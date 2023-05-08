import unittest
from reverse_cipher import reverse
class ReverseCypher(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse("chris"),"sirhc")

if __name__ == "__main__":
    unittest.main()