import unittest
import leapyear

class TestLeapYear(unittest.TestCase):
    def test_LeapYear(self):
        #Years divisble by 4 but not 100
        self.assertEqual(leapyear.leapyear(4), "is a leap year")
        self.assertEqual(leapyear.leapyear(16), "is a leap year")
        self.assertEqual(leapyear.leapyear(404), "is a leap year")

if __name__ == '__main__':
    unittest.main(verbosity=2)