class Zoo:
    opening_hours = None
    price_list = None

    def __init__(self, name, address, pavilions=None, shops=None):
        self.address = address
        self.name = name
        self.pavilions = pavilions
        self.shops = shops

    def enter(self):
        pass

    def feed(self):
        pass

    def pay_entry_fee(self):
        pass
