class Shop:

    def __init__(self, name, web_site, catalog):
        self.__name = name
        self.__web_site = web_site
        self.__catalog = catalog

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_web_site(self):
        return self.__web_site

    def set_web_site(self, web_site):
        self.__web_site = web_site

    def get_catalog(self):
        return self.__catalog

    def set_catalog(self, catalog):
        self.__catalog = catalog

    def to_string(self):
        return "Shop{" \
               + "name = '" \
               + self.__name \
               + "\'" \
               + ", web_site = '" \
               + self.__web_site \
               + "\'" \
               + ", catalog = " \
               + str(self.__catalog) \
               + "}"
