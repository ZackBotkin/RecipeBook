import unittest
from fridge import Ingredient, Fridge

class TestItemsAndFridge(unittest.TestCase):

    def setUp(self):
        FRIDGE_FILE='fridge.yaml'
        self.fridge = Fridge(FRIDGE_FILE)

    def test_one(self):
        self.assertEqual('foo', 'foo')
        self.fridge.print()

if __name__ == '__main__':
    unittest.main()
