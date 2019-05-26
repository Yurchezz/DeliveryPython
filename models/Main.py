from sqlite3.dbapi2 import Date
from managers.ShopManager import ShopManager
from models.Bus import Bus
from models.BusDelivery import BusDelivery
from models.HouseWife import HouseWife
from models.Plane import Plane
from models.Train import Train
from models.Location import Location
from models.PlaneDelivery import PlaneDelivery
from models.TrainDelivery import TrainDelivery
from models.Book import Book
from models.MacBook import MacBook
from models.ComputerMouse import ComputerMouse
from models.Shop import Shop


def main():

    start = Location(
        100,
        200
    )
    end = Location(
        200,
        200
    )

    anna = HouseWife(
        "Anna",
        end,
        1000,
        "0"
    )

    ant25 = Plane(
        "ANT25",
        10000,
        10
    )
    ant20 = Plane(
        "ant20",
        5000,
        10
    )

    inter_city = Train(
        "InterCity",
        15
    )
    chs2 = Train(
        "ChS2",
        15
    )

    sprinter = Bus(
        "Sprinter",
        200
    )
    double_decker = Bus(
        "Double Decker",
        100
    )

    delivery_date = Date(
        2019,
        4,
        21
    )

    urk_air_transport = PlaneDelivery(
        "SlavaUkraini",
        100,
        1220,
        start,
        end,
        ant25,
        delivery_date,
        anna
    )
    pl_air_transport = PlaneDelivery(
        "SmertVorogam",
        100,
        200,
        start,
        end,
        ant20,
        Date(2019, 4, 22),
        anna
    )

    urk_railway = TrainDelivery(
        "UkrRailway",
        1000,
        120,
        start,
        end,
        inter_city,
        Date(2020, 4, 21),
        anna
    )
    pl_railway = TrainDelivery(
        "PlRailway",
        100,
        109,
        start,
        end,
        chs2,
        Date(2019, 5, 27),
        anna
    )

    fed_ex = BusDelivery(
        "FedEx",
        100,
        1000,
        start,
        end,
        sprinter,
        Date(2025, 4, 21),
        anna
    )
    dhl = BusDelivery(
        "dhl",
        200,
        57,
        start,
        end,
        double_decker,
        Date(2030, 1, 2),
        anna
    )

    taras_bulba = Book(
        "Taras Bulba",
        500,
        400,
        "Nikolya Gogol",
        urk_air_transport
    )
    kobzar = Book(
        "Kobzar",
        700,
        1000,
        "Taras Shevchenko",
        pl_air_transport
    )
    garry_potter = Book(
        "Garry Potter",
        100,
        250,
        "Joah Rouling",
        urk_railway
    )

    pro_retina_13 = MacBook(
        "Pro Retina 13",
        1250,
        13,
        13,
        urk_railway
    )
    pro_retina_15 = MacBook(
        "Pro Retina 15",
        2250,
        15,
        17,
        fed_ex
    )
    air_retina_13 = MacBook(
        "Air Retina 13",
        1200,
        13,
        13,
        pl_railway
    )

    g403 = ComputerMouse(
        "Logitech g403",
        60,
        5,
        2,
        dhl
    )
    netscroll120 = ComputerMouse(
        "Genius netscroll 120",
        5,
        2,
        1,
        dhl
    )
    razer_champion = ComputerMouse(
        "Razor Champion",
        100,
        10,
        2,
        dhl
    )

    marta = HouseWife(
        "Marta",
        end,
        1000,
        "BOOKS"
    )
    nina = HouseWife(
        "Nina",
        end,
        100,
        "PANS"
    )

    amazon_catalog = [
        taras_bulba,
        kobzar,
        pro_retina_13,
        g403,
        netscroll120
    ]

    amazon_clients = [
        marta,
        nina
    ]

    amazon = Shop(
        "Amazon",
        "amazon.com",
        amazon_catalog
    )

    amazon_manager = ShopManager(
        amazon_clients,
        amazon
    )

    # amazon_manager.find_delivery_type("SmertVorogam")
    # amazon_manager.find_goods_range(100, 1000)

    # amazon_manager.sort_by_delivery_duration(True)
    # amazon_manager.show_catalog()

    # amazon_manager.sort_by_delivery_duration(False)
    # amazon_manager.show_catalog()

    # amazon_manager.sort_by_arrival_date(True)
    # amazon_manager.show_catalog()


if __name__ == "__main__":
    main()
