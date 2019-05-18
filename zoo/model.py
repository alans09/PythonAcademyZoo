from zoo import db


class Zoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    opening_hours = db.Column(db.String)
    price_list = db.Column(db.String)
    name = db.Column(db.String)

    pavilions = db.relationship('Pavilion', backref='zoo', lazy=True)
    shops = db.relationship('Shop', backref='zoo', lazy=True)

    def __init__(self, opening_hours, price_list, name):
        self.opening_hours = opening_hours
        self.price_list = price_list
        self.name = name


class Pavilion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    name = db.Column(db.String, unique=True)
    zoo_id = db.Column(db.Integer, db.ForeignKey('zoo.id'), nullable=False)

    animals = db.relationship('Animals', backref='pavilion', lazy=True)

    def __init__(self, type_, name, zoo_id):
        self.type = type_
        self.name = name
        self.zoo_id = zoo_id


class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    name = db.Column(db.String, unique=True)
    goods = db.Column(db.String)
    zoo_id = db.Column(db.Integer, db.ForeignKey('zoo.id'), nullable=False)

    def __init__(self, type_, name, goods, zoo_id):
        self.type = type_
        self.name = name
        self.goods = goods
        self.zoo_id = zoo_id



class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    sex = db.Column(db.String)
    type = db.Column(db.String)
    description = db.Column(db.String)
    diet = db.Column(db.String)

    pavilion_id = db.Column(db.Integer, db.ForeignKey('pavilion.id'), nullable=False)

    def __init__(self, name, age, sex, type_, description, diet, pavilion_id):
        self.name = name
        self.age = age
        self.sex = sex
        self.type = type_
        self.description = description
        self.diet = diet
        self.pavilion_id = pavilion_id

    def get_info(self):
        return(self.name, self.age, self.sex)


def init_database():
    db.create_all()
    # vygenerujeme zoo
    zoo = Zoo("opening hours", "price list", "moja zoo")
    # vygenerujeme pavilony
    water = Pavilion("Vodny pavilon", "water1", 1)
    sand = Pavilion("Piesocny pavilon", "sand1", 1)
    grass = Pavilion("Travnaty pavilon", "grass", 1)
    # vygenerujeme zvierata
    meerkat1 = Animals("Karolinka", 3, "F", "meerkat", "meerkat description", "grass, small insect", 2)
    meerkat2 = Animals("Nadezda", 3, "F", "meerkat", "meerkat description", "grass, small insect", 2)
    toad = Animals("Julius", 5, "M", "spadefoot toad", "toad description", "insect", 2)
    octopus1 = Animals("Nastasia", 11, "F", "giant octopus", "description of russion octopus", "fish", 1)
    octopus2 = Animals("Nemo", 12, "M", "giant octopus", "description of russion octopus", "fish", 1)
    grasshopper = Animals("Neo", 1, "M", "grasshopper", "description of grasshopper", "grass", 3)

    db.session.add(zoo)
    db.session.add(water)
    db.session.add(sand)
    db.session.add(grass)
    db.session.add(meerkat1)
    db.session.add(meerkat2)
    db.session.add(toad)
    db.session.add(octopus1)
    db.session.add(octopus2)
    db.session.add(grasshopper)

    db.session.commit()


if __name__ == "__main__":
    init_database()
