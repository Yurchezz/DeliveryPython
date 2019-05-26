class Client:
    def __init__(self, name, home, cash):
        self.__name = name
        self.__home = home
        self.__cash = cash

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_home(self):
        return self.__home

    def set_home(self, home):
        self.__home = home

    def get_cash(self):
        return self.__cash

    def set_cash(self, cash):
        self.__cash = cash

    def to_string(self):
        return "Client{"\
               + "name = '" \
               + self.__name \
               + "\'" \
               + ", home = " \
               + self.__home \
               + ", cash = " \
               + str(self.__cash) \
               + "}"
