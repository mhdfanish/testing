import unittest
from grade import mark

class testmar(unittest.TestCase):
    def testAdd(self):
        self.assertTrue(90,"A")
    def testAdd(self):
        self.assertTrue(80,"B")
    def testAdd(self):
        self.assertTrue(70,"C")
    def testAdd(self):
        self.assertTrue(60,"D")

if __name__=='__main__':
    unittest.main()