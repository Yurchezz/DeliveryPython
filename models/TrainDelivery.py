from models.Delivery import Delivery


class TrainDelivery(Delivery):

    def __init__(self, name, price, duration, start_storage, final_storage, train, arrival, client):
        super(TrainDelivery, self).__init__(name, price, duration, arrival, client)
        self.__start_storage = start_storage
        self.__final_storage = final_storage
        self.__train = train

    def get_start_storage(self):
        return self.__start_storage

    def set_start_storage(self, start_storage):
        self.__start_storage = start_storage

    def get_final_storage(self):
        return self.__final_storage

    def set_final_storage(self, final_storage):
        self.__final_storage = final_storage

    def get_train(self):
        return self.__train

    def set_train(self, train):
        self.__train = train

    def to_string(self):
        return "TrainDelivery{" \
               + "start_storage = " \
               + self.__start_storage.to_string() \
               + ", final_storage = " \
               + self.__final_storage.to_string() \
               + ", train = " \
               + self.__train.to_string() \
               + "}"
