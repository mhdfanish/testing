import unittest
from grade import mark

class testmar(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(mark(90)," grade A")
    def testAdd(self):
        self.assertEqual(mark(80),"grade B")
    def testAdd(self):
        self.assertEqual(mark(70),"grade C")
    def testAdd(self):

        self.assertEqual(mark(60),"grade D")

if __name__=='__main__':
    unittest.main()