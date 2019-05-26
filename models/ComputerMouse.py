from models.Good import Good


class ComputerMouse(Good):

    def __init__(self, name, price, button_count, cable_length, delivery):
        super(ComputerMouse, self).__init__(name, price, delivery)
        self.__button_count = button_count
        self.__cable_length = cable_length

    def get_button_count(self):
        return self.__button_count

    def set_button_count(self, button_count):
        self.__button_count = button_count

    def get_cable_length(self):
        return self.__cable_length

    def set_cable_length(self, cable_length):
        self.__cable_length = cable_length
