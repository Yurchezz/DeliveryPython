from models.Good import Good


class Book(Good):

    def __init__(self, name, price, page_count, author, delivery):
        super(Book, self).__init__(name, price, delivery)
        self.__page_count = page_count
        self.__author = author

    def get_page_count(self):
        return self.__page_count

    def set_page_count(self, page_count):
        self.__page_count = page_count

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author
