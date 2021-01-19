import unittest
from fridge import Fridge, Ingredient, Recipe

class TestItemsAndFridge(unittest.TestCase):

    def setUp(self):
        RECIPE_FILE='recipes/enchiladas.yaml'
        FRIDGE_FILE='fridge.yaml'
        self.recipe = Recipe(RECIPE_FILE)
        self.fridge = Fridge(FRIDGE_FILE)

    def test_one(self):
        pass

if __name__ == '__main__':
    unittest.main()
