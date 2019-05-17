from unittest import TestCase
from zoo import *
from animals import *
from shop import *


class TestZoo(TestCase):
    def setUp(self):
        meerkat = Meerkat("Karol", "3", "M")
        meerkatF = Meerkat("Natalia", "2", "F")
        sand1 = Pavilion("Sand", "sand1", [meerkat, meerkatF])
        dingo1 = Dingo("Stefan", "12", "M")
        sand1.add_animal(dingo1)
        self.zoo = Zoo("Tomas's ZOO", "Einsteinova 23, Bratislava", [sand1])

    def test_attributes(self):
        self.assertEqual(self.zoo.name, "Tomas's ZOO")
        self.assertEqual(self.zoo.address, "Einsteinova 23, Bratislava")

    def test_enter(self):
        self.zoo.enter()
        self.assertTrue(self.zoo.entered)

    def test_feed(self):
        self.fail()

    def test_pay_entry_fee(self):
        self.fail()
