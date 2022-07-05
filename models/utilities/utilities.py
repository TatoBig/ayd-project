from ..store import Store
from random import randint


class Utilities:
    def __init__(self):
        self.__store: Store = Store()

    def random_border_location(self):
        border = randint(1, 4)
        if border == 1:
            rand_x = randint(0, self.__store.get_width())
            rand_y = 0
        elif border == 2:
            rand_x = randint(0, self.__store.get_width())
            rand_y = self.__store.get_height()
        elif border == 3:
            rand_x = 0
            rand_y = randint(0, self.__store.get_height())
        else:
            rand_x = self.__store.get_width()
            rand_y = randint(0, self.__store.get_height())

        return [rand_x, rand_y]

    def random_location(self):
        rand_x = randint(15, self.__store.get_width())
        rand_y = randint(15, self.__store.get_height())

        return [rand_x, rand_y]
