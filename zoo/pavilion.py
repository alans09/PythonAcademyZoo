from zoo.animal import Animal


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

    def list_animals(self):
        """
        a) pavilon1
        b) pavilon2
        """
        ret = ""
        for idx, animal in enumerate(self.animals):
            ret += f"{idx:<5} {animal.name:^50}\n"
        return ret

    def remove_animal(self, animal):
        pass