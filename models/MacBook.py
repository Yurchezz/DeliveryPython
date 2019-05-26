from models.Good import Good


class MacBook(Good):

    def __init__(self, name, price, display_diagonal, manufacture_year, delivery):
        super(MacBook, self).__init__(name, price, delivery)
        self.__display_diagonal = display_diagonal
        self.__manufacture_year = manufacture_year

    def get_display_diagonal(self):
        return self.__display_diagonal

    def set_display_diagonal(self, display_diagonal):
        self.__display_diagonal = display_diagonal

    def get_manufacture_year(self):
        return self.__manufacture_year

    def set_manufacture_year(self, manufacture_year):
        self.__manufacture_year = manufacture_year
