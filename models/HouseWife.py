from models.Client import Client


class HouseWife(Client):

    def __init__(self, name, home, cash, house_wife_preferences):
        super(HouseWife, self).__init__(name, home, cash)
        self.__house_wife_preferences = house_wife_preferences

    def get_house_wife_preferences(self):
        return self.__house_wife_preferences
