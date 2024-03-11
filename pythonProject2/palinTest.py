import unittest
from palin import isPalindrome

class testPalin(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(isPalindrome('malayalam'),True)
    def testAdd(self):
        self.assertEqual(isPalindrome('car'),False)
    def testAdd(self):
        self.assertEqual(isPalindrome('racecar'),True)