import unittest
from index import add, subtract

class TestOperation(unittest.TestCase):
    def test_add(self):
      self.assertEqual(add(4, 6), 10)
      self.assertEqual(add(8, 8), 16)
      self.assertEqual(add(-1, 1), 0)
    def test_subtract(self):
       self.assertEqual(subtract(4, 6), -2)
       self.assertEqual(subtract(8, 8), 0)
    

if __name__ == '__main__':
    unittest.main()