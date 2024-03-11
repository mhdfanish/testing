import unittest
from grade import mark

class testmar(unittest.TestCase):
    def testAdd(self):
        self.assertTrue(mark,msg="A")
    def testAdd(self):
        self.assertTrue(mark,msg="B")
    def testAdd(self):
        self.assertTrue(mark,msg="C")
    def testAdd(self):
        self.assertTrue(mark,msg="D")

if __name__=='__main__':
    unittest.main()