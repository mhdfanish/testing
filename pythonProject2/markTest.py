import unittest
from grade import mark

class testmar(unittest.TestCase):
    def testAdd(self):
        self.assertTrue(90,msg="A")
    def testAdd(self):
        self.assertTrue(80,msg="B")
    def testAdd(self):
        self.assertTrue(70,msg="C")
    def testAdd(self):
        self.assertTrue(60,msg="D")

if __name__=='__main__':
    unittest.main()