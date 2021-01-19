import yaml

class Ingredient(object):

    def __init__(self, description, date_aquired, amount_left):
        self.description = description
        self.date_aquired = date_aquired
        self.amount_left = amount_left

class Recipe(object):

    def __init__(self, recipe_file):
        self.ingredients = []
        self._init_from_file(recipe_file)

    def _ingredients_from_yaml(self, ingredients):
        pass

    def _init_from_file(self, recipe_file):
        with open(recipe_file) as file:
            recipe_yaml = yaml.load(
                file, Loader= yaml.FullLoader
            )

class Fridge(object):

    def __init__(self, fridge_file):
        self.ingredients = {}
        self._init_from_file(fridge_file)

    def _ingredient_from_yaml(self, _key, _yaml):
        return Ingredient(
            _key, _yaml['date aquired'], _yaml['amount left']
        )

    def _init_from_file(self, fridge_file):
        with open(fridge_file) as file:
            fridge_yaml = yaml.load(
                file, Loader= yaml.FullLoader
            )
            for _key, _yaml in fridge_yaml.items():
                if _key not in self.ingredients:
                    self.ingredients[_key] = self._ingredient_from_yaml(_key, _yaml)

    def get_missing_ingredients(self):
        pass

