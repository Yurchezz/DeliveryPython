class Plane:

    def __init__(self, mark, max_height, tonnage):
        self.__mark = mark
        self.__max_height = max_height
        self.__tonnage = tonnage

    def get_mark(self):
        return self.__mark

    def set_mark(self, mark):
        self.__mark = mark

    def get_max_height(self):
        return self.__max_height

    def set_max_height(self, max_height):
        self.__max_height = max_height

    def get_tonnage(self):
        return self.__tonnage

    def set_tonnage(self, tonnage):
        self.__tonnage = tonnage

    def to_string(self):
        return "Plane{" \
               + "mark = '" \
               + self.__mark \
               + "\'" \
               + ", max_height = " \
               + str(self.__max_height) \
               + ", tonnage = " \
               + str(self.__tonnage) \
               + "}"
