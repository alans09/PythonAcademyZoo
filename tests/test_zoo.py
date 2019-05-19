from unittest import TestCase
from zoo import *
from animals import *
from shop import *


class TestZoo(TestCase):
    def setUp(self):
        meerkat = Meerkat("Karol", "3", "M")
        meerkatF = Meerkat("Natalia", "2", "F")
        crocodile1 = Crocodile("Boris", "3", "M")
        crocodile2 = Crocodile("Nastasia", "3", "F")
        duck = Duck("Ruby", "1", "F")
        sand1 = Pavilion("Sand", "sand1", [meerkat, meerkatF])
        water = Pavilion("Water", "water1", [crocodile1, crocodile2, duck])
        shop = Shop("Souvenir","suv1","{'duck':12, 'crocodile':11}")
        self.zoo = Zoo("Tomas's ZOO", "Einsteinova 23, Bratislava", [sand1, water], [shop])

    def test_attributes(self):
        self.assertEqual(self.zoo.name, "Tomas's ZOO")
        self.assertEqual(self.zoo.address, "Einsteinova 23, Bratislava")
        self.assertEqual(self.zoo.price_list, {"Main-season": 12, "Off-season": 8})
        self.assertEqual(
            self.zoo.opening_hours,
            {
                "Monday - Friday": "11:00 - 17:00",
                "Saturday": "9:00 - 17:00",
                "Sunday": "Closed"
            }
        )

    def test_pavilions(self):
        self.assertEqual(len(self.zoo.pavilions), 2)

    def test_shops(self):
        self.assertEqual(len(self.zoo.shops), 1)

    def test_add_shop(self):
        test_shop = Shop("Test", "test", "{}")
        self.zoo.add_shop(test_shop)
        check = [ shop.name for shop in self.zoo.shops ]
        self.assertIn("test", check)

    def test_add_pavilion(self):
        test_pavilion = Pavilion("Test", "test")
        self.zoo.add_pavilion(test_pavilion)
        check = [ pavilion.name for pavilion in self.zoo.pavilions ]
        self.assertIn("test", check)

    def test_remove_pavilion(self):
        self.zoo.remove_pavilion("test")
        check = [ pavilion.name for pavilion in self.zoo.pavilions ]
        self.assertNotIn("test", check)

