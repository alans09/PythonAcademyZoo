from zoo.zoo import *
from zoo.animals import *


def show_main_menu():
    main_menu = [
        "1) Zobrazit otvaracie hodiny",
        "2) Zobrazit vstupne",
        "3) Zobrazit zoznam pavilonov",
        "4) Zobrazit zoznam obchodov",
        "5) Zobrazit zoznam zvierat",
        "e) Ukoncit program"
    ]
    for menu in main_menu:
        print(menu)
    print()


def show_opening_hours():
    print(zoo.show_opening_hours())


def show_entrance_fee():
    print(zoo.show_entrance_fees())


def show_pavilions_menu():
    print(zoo.list_pavilions())
    print(f"{'e':<20}{'Navrat do hlavneho menu':>20}\n")


def show_pavilions_list():
    selection = None
    while selection != "e":
        show_pavilions_menu()
        selection = input("Vyber cislo pre detail pavilonu alebo 'e' pre navrat spat:")
        if selection == "e":
            break
        if int(selection) in range(len(zoo.pavilions)):
            print(zoo.pavilions)
            print(zoo.pavilions[int(selection)].list_animals())
        else:
            print("Skus to este raz, neznama volba")
        print("=====")


def show_animals_menu():
    animals = []
    for pavilion in zoo.pavilions:
        animals += [animal for animal in pavilion.animals]
    for idx, animal in enumerate(animals):
        print(f"{idx:<5} {animal.name:^20} {animal.__class__.__name__:^20}")
    print(f"{'e':<5} {'Navrat do hlavneho menu':>20}")
    return animals


def show_animals_list():
    selection = None
    while selection != "e":
        animals = show_animals_menu()
        selection = input("Vyber cislo pre detail zvierata alebo 'e' pre navrat do hlavneho menu")
        if selection == "e":
            break
        if int(int(selection) in range(len(animals))):
            print(animals[int(selection)])
        else:
            print("Skus to este raz, neznama volba")
        print("=====")


def show_detail(id_):
    if id_ == 1:
        show_opening_hours()
    elif id_ == 2:
        show_entrance_fee()
    elif id_ == 3:
        show_pavilions_list()
    elif id_ == 4:
        print("NOT IMPLEMENTED YET")
    elif id_ == 5:
        show_animals_list()
    print("=====")


def main():
    # najprv si vytvorim data
    global zoo
    meerkat = Meerkat("Karol", "3", "M")
    meerkatF = Meerkat("Natalia", "2", "F")
    crocodile1 = Crocodile("Boris", "3", "M")
    crocodile2 = Crocodile("Nastasia", "3", "F")
    duck = Duck("Ruby", "1", "F")
    sand1 = Pavilion("Sand", "sand1", [meerkat, meerkatF])
    water = Pavilion("Water", "water1", [crocodile1, crocodile2, duck])
    shop = Shop("Souvenir" ,"suv1" ,"{'duck':12, 'crocodile':11}")
    zoo = Zoo("Tomas's ZOO", "Einsteinova 23, Bratislava", [sand1, water], [shop])

    # hlavna logika
    selection = None
    while selection != "e":
        show_main_menu()
        selection = input("Vyber co chces robit: ")
        if selection == "e":
            print("Dakujeme za navstevu zoo")
            break
        elif selection in ["1", "2", "3", "4", "5"]:
            show_detail(int(selection))
        else:
            print("Nepoznam taku moznost")
            print()

if __name__ == "__main__":
    main()


