class Location:

    def __init__(self, longitude, latitude):
        self.__longitude = longitude
        self.__latitude = latitude

    def get_longitude(self):
        return self.__longitude

    def set_longitude(self, longitude):
        self.__longitude = longitude

    def get_latitude(self):
        return self.__latitude

    def set_latitude(self, latitude):
        self.__latitude = latitude

    def to_string(self):
        return "Location{" \
               + "longitude = " \
               + str(self.__longitude) \
               + ", latitude = " \
               + str(self.__latitude) \
               + "}"
