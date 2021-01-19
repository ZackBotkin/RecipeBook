import os
import yaml

class Ingredient(object):

    def __init__(self, description, date_aquired, amount):
        self.description = description
        self.date_aquired = date_aquired
        self.amount = amount


class RecipeBook(object):

    def __init__(self, recipe_directory=None, associated_fridge_file=None):
        self.recipes = []
        if recipe_directory is not None:
            self._build_recipes_from_disk(recipe_directory)
        self.fridge = Fridge(associated_fridge_file)

    def _build_recipes_from_disk(self, directory):
        for _filename in os.listdir(directory): 
            recipe = Recipe('%s/%s' % (directory, _filename))
            self.recipes.append(recipe)

    def get_possible_recipes(self):
        possible_recipes = []
        for recipe in self.recipes:
            if self.fridge.can_make_recipe(recipe):
                possible_recipes.append(recipe.description)
        return possible_recipes

    ## TODO : this is the main question the app solves haha
    def get_optimal_recipe(self):
        pass


class Recipe(object):

    def __init__(self, recipe_file=None):
        self.ingredients = []
        if recipe_file:
            self._init_from_file(recipe_file)

    def _init_from_file(self, recipe_file):
        with open(recipe_file) as file:
            recipe_yaml = yaml.load(
                file, Loader= yaml.FullLoader
            )
            ingredients = recipe_yaml['ingredients']
            for ingredient in ingredients:
                self.ingredients.append(
                    Ingredient(ingredient['name'], None, ingredient['amount'])
                )


class Fridge(object):

    def __init__(self, fridge_file=None):
        self.ingredients = {}
        if fridge_file:
            self._init_from_file(fridge_file)

    def _ingredient_from_yaml(self, _key, _yaml):
        return Ingredient(
            _key, _yaml['date added'], _yaml['amount']
        )

    def _init_from_file(self, fridge_file):
        with open(fridge_file) as file:
            fridge_yaml = yaml.load(
                file, Loader= yaml.FullLoader
            )
            for _key, _yaml in fridge_yaml.items():
                if _key not in self.ingredients:
                    self.ingredients[_key] = self._ingredient_from_yaml(_key, _yaml)


    def can_make_recipe(self, recipe):
        for ingredient in recipe.ingredients:
            if ingredient.description not in self.ingredients:
                return False
        return True

    def get_missing_ingredients(self, recipe):
        missing_ingredients = []
        for ingredient in recipe.ingredients:
            if ingredient.description not in self.ingredients:
                missing_ingredients.append(ingredient.description)
        return missing_ingredients

