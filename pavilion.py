from animals import Animal


class Pavilion:
    def __init__(self, type_, name, animals=None):
        self.type = type_
        self.name = name
        self.animals = animals

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            return False
        if self.animals:
            self.animals.append(animal)
        else:
            self.animals = [animal]


    def remove_animal(self, animal):
        pass