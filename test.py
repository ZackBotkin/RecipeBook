import unittest
from fridge import Fridge, Ingredient, Recipe, RecipeBook

class TestItemsAndFridge(unittest.TestCase):

    def setUp(self):
        pass

    def test_can_make_recipes(self):

        recipe = Recipe()
        recipe.ingredients.append(Ingredient('peanut butter', None, '5 tablespoons'))
        recipe.ingredients.append(Ingredient('bread', None, '2 slices'))
        recipe.ingredients.append(Ingredient('jelly', None, '5 tablespoons'))

        fridge = Fridge()
        fridge.ingredients['peanut butter'] = Ingredient('peanut butter', None, '1 jar')
        fridge.ingredients['bread'] = Ingredient('bread', None, '1 loaf')
        self.assertFalse(fridge.can_make_recipe(recipe))

        fridge.ingredients['jelly'] = Ingredient('jelly', None, '1 jar')
        self.assertTrue(fridge.can_make_recipe(recipe))

    def test_get_missing_ingredients(self):

        recipe = Recipe()
        recipe.ingredients.append(Ingredient('peanut butter', None, '5 tablespoons'))
        recipe.ingredients.append(Ingredient('bread', None, '2 slices'))
        recipe.ingredients.append(Ingredient('jelly', None, '5 tablespoons'))

        fridge = Fridge()
        missing_ingredients = fridge.get_missing_ingredients(recipe)
        self.assertEqual(missing_ingredients, ['peanut butter', 'bread', 'jelly'])

        fridge.ingredients['peanut butter'] = Ingredient('peanut butter', None, '1 jar')
        missing_ingredients = fridge.get_missing_ingredients(recipe)
        self.assertEqual(missing_ingredients, ['bread', 'jelly'])

        fridge.ingredients['bread'] = Ingredient('bread', None, '1 loaf')
        missing_ingredients = fridge.get_missing_ingredients(recipe)
        self.assertEqual(missing_ingredients, ['jelly'])

        fridge.ingredients['jelly'] = Ingredient('jelly', None, '1 jar')
        missing_ingredients = fridge.get_missing_ingredients(recipe)
        self.assertEqual(missing_ingredients, [])

    def test_get_possible_recipes(self):

        RECIPE_DIR="recipes"
        FRIDGE_FILE="fridge.yaml"

        recipe_book = RecipeBook(RECIPE_DIR, FRIDGE_FILE) 



if __name__ == '__main__':
    unittest.main()
