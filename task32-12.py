import unittest
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "should be abs number value")
        
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be abs number value")
    
if __name__ == "__main__":
    unittest.main()