from pavilion import *
from shop import *
from animals import *


class Zoo:
    opening_hours = {
        "Monday - Friday": "11:00 - 17:00",
        "Saturday": "9:00 - 17:00",
        "Sunday": "Closed"
    }
    price_list = {"sezona": 12}
    entered = False

    def __init__(self, name, address, pavilions=None, shops=None):
        self.address = address
        self.name = name
        self.pavilions = pavilions
        self.shops = shops

    def show_opening_hours(self):
        ret = ""
        for key in self.opening_hours:
            ret += f"{key:<20}{self.opening_hours[key]:>20}\n"
        return ret

    def change_opening_hours(self, key, value):
        self.opening_hours[key] = value

    def list_pavilions(self):
        """
        a) pavilon1
        b) pavilon2
        """
        ret = ""
        for idx, pavilion in enumerate(self.pavilions):
            ret += f"{idx:<5} {pavilion.name:^50}"
        return ret

    def add_pavilion(self, pavilion):
        if not isinstance(pavilion, Pavilion):
            return False
        if self.pavilions:
            self.pavilions.append(pavilion)
        else:
            self.pavilions = [pavilion]

    def remove_pavilion(self, name):
        if self.pavilions:
            for idx, pavilion in enumerate(self.pavilions):
                if pavilion.name == name:
                    self.pavilions.pop(idx)
                    break
        else:
            # nezmazal som ziadny pavilon
            return False

    def add_shop(self, shop):
        if not isinstance(shop, Shop):
            return False
        if self.shops:
            self.shops.append(shop)
        else:
            self.shops = [shop]

    def enter(self):
        self.entered = True

    def feed(self):
        pass

    def pay_entry_fee(self):
        pass


if __name__ == "__main__":
    meerkat = Meerkat("Karol", "3", "M")
    meerkatF = Meerkat("Natalia", "2", "F")
    sand1 = Pavilion("Sand", "sand1", animals=[meerkat, meerkatF])
    dingo1 = Dingo("Stefan", "12", "M")
    zoo = Zoo("Zoo1", "Einsteinova23, Bratislava", pavilions=[sand1])
    sand1.add_animal(dingo1)
    for animal in zoo.pavilions[0].list_animals():
        print(animal)
    print(zoo.list_pavilions())
