class Animal:
    description = None

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        raise NotImplementedError("Potrebujes definovat metodu")

    def eat(self):
        return "ham ham"

    def sound(self):
        raise NotImplementedError("Potrebujes definovat zvuk")


class Dingo(Animal):
    description = """
    Dingo austrálsky (iné názvy: pes dingo, dingo; lat. Canis dingo, Canis lupus dingo)
    je austrálska psovitá šelma, väčšinou chápaná ako poddruh vlka dravého (Canis lupus dingo),
    niekedy ako samostatný druh Canis dingo.
        
                         .
                        / V\
                      / `  /
                     <<   |
                     /    |
                   /      |
                 /        |
               /    \  \ /
              (      ) | |
      ________|   _/_  | |
    <__________\______)\__)
    """

    def __str__(self):
        return f"{self.description}\n\tMeno: {self.name}, Vek: {self.age}, Pohlavie: {self.sex}"

    def sound(self):
        return "howl"


class Tiger(Animal):
    description = """
    Tiger džungľový (iné názvy: tiger pruhovaný, tiger pásavý, tiger, zastarano tiger kráľovský, lat. Panthera tigris)
    je cicavec z čeľade mačkovité (Felidae), jedna zo štyroch veľkých mačiek rodu Panthera.  
    
                         __,,,,_
          _ __..-;''`--/'/ /.',-`-.
      (`/' ` |  \ \ \\ / / / / .-'/`,_
     /'`\ \   |  \ | \| // // / -.,/_,'-,
    /<7' ;  \ \  | ; ||/ /| | \/    |`-/,/-.,_,/')
   /  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\'
   `-`  f/ ;      / __/ \__ `/ |__/ |
        `-'      |  -| =|\_  \  |-' |
              __/   /_..-' `  ),'  //
             ((__.-'((___..-'' \__.'
    """

    def __str__(self):
        return f"{self.description}\n\tMeno: {self.name}, Vek: {self.age}, Pohlavie: {self.sex}"

    def sound(self):
        return "grrrrrr"


class Crocodile(Animal):
    description = """
    Krokodíl morský alebo krokodíl cejlónsky alebo krokodíl indopacifický (lat. Crocodylus porosus)
    je plaz z čeľade krokodílovitých. Je najväčší z krokodílov a zároveň je dnes najväčším a najmohutnejším plazom
    na svete. Je jedným z mála krokodílov, ktoré sa často vydávajú ďaleko na more. 
    
              _  _
             / \/ \-._   _.-'^'^^'^^'^^"^^'-.
     .OO.----'\o/\o/   `-'                /^  ^^-._
    (    `                 \             |    _    ^^-._
     VvvvvvvVvv`___...)_/  /_/_/_/_/_/_/_/\  (__________^^-.
      `^^^^^^^^`       /  /                >  >        _`)  )
                      (((`                (((`        `'--'^
    """

    def __str__(self):
        return f"{self.description}\n\tMeno: {self.name}, Vek: {self.age}, Pohlavie: {self.sex}"

    def sound(self):
        return "snap"


class Meerkat(Animal):
    description = """
    Surikata alebo staršie surikáta (lat. Suricata) je rod z čeľade mungovité.    
    Zahŕňa recentný druh surikata vlnkavá (Suricata suricatta) a vyhynutý druh Suricata major. 
    Vyhynutý druh sa od recentného odlišuje predovšetkým veľkosťou a chrupom. 
    Niektorí autori vyhynutý druh zaraďujú pod surikatu vlnkavú. Všetky súčasné aj fosílne nálezy 
    (fosílne nálezy recentného aj vyhynutého druhu) pochádzajú z južnej Afriky. 
    """

    def __str__(self):
        return f"{self.description}\n\tMeno: {self.name}, Vek: {self.age}, Pohlavie: {self.sex}"

    def sound(self):
        return "purrrr"


class Duck(Animal):
    description = """
    Kačica divá alebo kačica veľká (lat. Anas platyrhynchos) je zúbkozobec z čeľade kačicovité (Anatidae).
    Kačica divá je najčastejšie a najďalej rozšírený druh kačice. Vyskytuje sa na celej severnej pologuli, 
    od Európy cez Áziu až do Severnej Ameriky. Na Novom Zélande je dovezená a skrížená s domácou Anas superciliosa.
    V mnohých mestách sa vyskytujú kačice divé, ktoré sú skrížené s kačicou domácou a vyznačujú sa odlišným sfarbením.
    Je to najbežnejšia kačica Európy a hniezdi aj nad 2 000 m n. m..
               __
             <(o )___
              ( ._> /
               `---'  
    """

    def __str__(self):
        return f"{self.description}\n\tMeno: {self.name}, Vek: {self.age}, Pohlavie: {self.sex}"

    def sound(self):
        return "quaaack"

