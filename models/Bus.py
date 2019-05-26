class Bus:

    def __init__(self, mark, max_speed):
        self.__mark = mark
        self.__max_speed = max_speed

    def get_mark(self):
        return self.__mark

    def set_mark(self, mark):
        self.__mark = mark

    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def to_string(self):
        return "Bus{"\
               + "mark = '" \
               + self.__mark \
               + "', max_speed = " \
               + str(self.__max_speed) \
               + "}"
