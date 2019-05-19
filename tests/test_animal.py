from unittest import TestCase
from zoo.animal import *


class TestAnimal(TestCase):
    def setUp(self):
        self.animal = Animal("Simple Animal", 4, "M")

    def test_simple_animal(self):
        self.assertEqual(self.animal.name, "Simple Animal")
        self.assertEqual(self.animal.age, 4)
        self.assertEqual(self.animal.sex, "M")

    def test_print_simple(self):
        with self.assertRaises(NotImplementedError):
            print(self.animal)

    def test_sound_simple(self):
        self.assertRaises(NotImplementedError, self.animal.sound)
