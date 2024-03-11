import unittest
from vote import vot

class testvot(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(vot(40),"you are eligible for voting")

    def testAdd(self):
            self.assertEqual(vot(17), "you are not eligible for vote")

    def testAdd(self):
                self.assertEqual(vot(55), "you are eligible for voting")

if __name__=='__main__':
    unittest.main()