from models import Shop


class ShopManager:

    def __init__(self, clients, shop):
        self.__clients = clients
        self.__shop = shop

    def find_delivery_type(self, delivery_name):
        for good in self.__shop.get_catalog():
            if good.get_delivery().get_name() == delivery_name:
                print(good.get_name())

    def find_goods_range(self, lower, higher):
        for good in self.__shop.get_catalog():
            if higher > good.get_price() > lower:
                print(good.get_name())

    def sort_by_delivery_duration(self, from_lower_to_higher):
        if from_lower_to_higher:
            self.__shop.get_catalog().sort(key=lambda x: x.get_delivery().get_duration())
            return self.__shop.get_catalog()

        else:
            self.__shop.get_catalog().sort(key=lambda x: x.get_delivery().get_duration(), reverse=True)
            return self.__shop.get_catalog()

    def sort_by_delivery_price(self, from_lower_to_higher):
        if from_lower_to_higher:
            self.__shop.get_catalog().sort(key=lambda x: x.get_delivery().get_price())
            return self.__shop.get_catalog()

        else:
            self.__shop.get_catalog().sort(key=lambda x: x.get_delivery().get_price(), reverse=True)
            return self.__shop.get_catalog()

    def sort_by_arrival_date(self, from_lower_to_higher):
        if from_lower_to_higher:
            self.__shop.get_catalog().sort(key=lambda x: x.get_delivery().get_arrival())
            return self.__shop.get_catalog()

        else:
            self.__shop.get_catalog().sort(key=lambda x: x.get_delivery().get_arrival(), reverse=True)
            return self.__shop.get_catalog()

    def show_catalog(self):
        for good in self.__shop.get_catalog():
            print(good.to_string())
