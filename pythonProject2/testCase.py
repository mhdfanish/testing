import unittest
from test import add
from test import subtract
from test import mult
from test import div
class testCal(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(add(10,10),20)
    def testAdd(self):
        self.assertEqual(subtract(10,5),5)
    def testAdd(self):
        self.assertEqual(mult(10,10),100)
    def testAdd(self):
        self.assertEqual(div(10,5),2.0)
if __name__=='__main__':
    unittest.main()