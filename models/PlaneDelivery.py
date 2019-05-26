from models.Delivery import Delivery


class PlaneDelivery(Delivery):

    def __init__(self, name, price, duration, start_airport, final_airport, plane, arrival, client):
        super(PlaneDelivery, self).__init__(name, price, duration, arrival, client)
        self.__start_airport = start_airport
        self.__final_airport = final_airport
        self.__plane = plane

    def get_start_airport(self):
        return self.__start_airport

    def set_start_airport(self, start_airport):
        self.__start_airport = start_airport

    def get_final_airport(self):
        return self.__final_airport

    def set_final_airport(self, final_airport):
        self.__final_airport = final_airport

    def get_plane(self):
        return self.__plane

    def set_plane(self, plane):
        self.__plane = plane

    def to_string(self):
        return "PlaneDelivery{" \
               + "start_airport = " \
               + self.__start_airport.to_string() \
               + ", final_storage = " \
               + self.__final_airport.to_string() \
               + ", plane = " \
               + self.__plane.to_string() \
               + "}"
