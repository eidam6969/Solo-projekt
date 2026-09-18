import unittest

def text_na_velka(text):
    return text.isupper()
    
class TestVelka(unittest.TestCase):

    def test_spravny_prevod(self):
        self.assertTrue(text_na_velka("NEVIM"))
        self.assertTrue(text_na_velka("AHOJ"))

if __name__ == "__main__":
    unittest.main()
