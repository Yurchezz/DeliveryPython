from models.Delivery import Delivery


class BusDelivery(Delivery):

    def __init__(self, name, price, duration, start_storage, final_storage, bus, arrival, client):
        super(BusDelivery, self).__init__(name, price, duration, arrival, client)
        self.__start_storage = start_storage
        self.__final_storage = final_storage
        self.__bus = bus

    def get_start_storage(self):
        return self.__start_storage

    def set_start_storage(self, start_storage):
        self.__start_storage = start_storage

    def get_final_storage(self):
        return self.__final_storage

    def set_final_storage(self, final_storage):
        self.__final_storage = final_storage

    def get_bus(self):
        return self.__bus

    def set_bus(self, bus):
        self.__bus = bus

    def to_string(self):
        return "BusDelivery{" \
               + "start_storage = " \
               + self.__start_storage.to_string() \
               + ", final_storage = " \
               + self.__final_storage.to_string() \
               + ", bus = " \
               + self.__bus.to_string() \
               + "}"
