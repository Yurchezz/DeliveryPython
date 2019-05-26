from sqlite3.dbapi2 import Date


class Delivery:
    def __init__(self, name, price, duration, arrival, client):
        self.__name = name
        self.__price = price
        self.__duration = duration
        self.__arrival = arrival
        self.__client = client

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_arrival(self):
        return self.__arrival

    def set_arrival(self, arrival):
        self.__arrival = arrival

    def get_client(self):
        return self.__client

    def set_client(self, client):
        self.__client = client

    def to_string(self):
        return "Delivery {" \
               + "| name = '" \
               + self.__name \
               + ", price = " \
               + str(self.__price)\
               + ", duration = " \
               + str(self.__duration) \
               + ", client = " \
               + self.__client.to_string() \
               + ", arrival = " \
               + str(self.__arrival) \
               + ' | }'
