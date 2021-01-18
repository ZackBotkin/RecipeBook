import yaml


class Item(object):
    def __init__(self, description, date_aquired, amount_left):
        self.description = description
        self.date_aquired = date_aquired
        self.amount_left = amount_left

class Fridge(object):

    def __init__(self, fridge_file):
        self.fridge = {}
        self._init_from_file(fridge_file)

    def _item_from_yaml(self, _key, _yaml):
        return Item(
            _key, _yaml['date aquired'], _yaml['amount left']
        )

    def _init_from_file(self, fridge_file):
        with open(fridge_file) as file:
            fridge_yaml = yaml.load(
                file, Loader= yaml.FullLoader
            )
            for _key, _yaml in fridge_yaml.items():
                if _key not in self.fridge:
                    self.fridge[_key] = self._item_from_yaml(_key, _yaml)

    def print(self):
        for _key, _yaml in self.fridge.items():
            print(_key)

