class Train:

    def __init__(self, mark, railway_carriage_count):
        self.__mark = mark
        self.__railway_carriage_count = railway_carriage_count

    def get_mark(self):
        return self.__mark

    def set_mark(self, mark):
        self.__mark = mark

    def get_railway_carriage_count(self):
        return self.__railway_carriage_count

    def set_mark(self, railway_carriage_count):
        self.__railway_carriage_count = railway_carriage_count

    def to_string(self):
        return "Train{" \
               + "mark = '" \
               + self.__mark \
               + "\'" \
               + ", railway_carriage_count = " \
               + str(self.__railway_carriage_count) \
               + "}"
