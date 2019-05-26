class Good:

    def __init__(self, name, price, delivery):
        self.__name = name
        self.__price = price
        self.__delivery = delivery

    def get_delivery(self):
        return self.__delivery

    def set_delivery(self, delivery):
        self.__delivery = delivery

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def to_string(self):
        return "Good {" \
               + "| name = '" \
               + self.__name \
               + ", | arrival date = " \
               + str(self.__delivery.get_arrival()) \
               + ", | delivery duration = " \
               + str(self.__delivery.get_duration()) \
               + ", | delivery price = " \
               + str(self.__delivery.get_price()) \
               + '}'
