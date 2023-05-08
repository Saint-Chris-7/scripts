import unittest


from verman_cipher_decrypt import decrypt

class TestVermanDecrypt(unittest.TestCase):
    def test(self):
        self.assertEqual(decrypt("ÄÊÕÍØ","chris"),"abcde")
if __name__ == "__main__":
    unittest.main()