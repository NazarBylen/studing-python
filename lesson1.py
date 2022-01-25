from datetime import datetime
import union as union


class Fish:
    def __init__(self, name, price_in_uah_per_kilo, origin) -> None:
        self.name = "oseledets"
        self.price_in_uah_per_kilo = 11.2
        self.origin = "Norway"
        self.body_only = True
        self.weight = 100


class FishShop():

    fish_list = []
    def add_fish(self, name: str = "Unnamed fish",
                 price_in_uah_per_kilo: float = 100,
                 origin: str = "Unnamed country"):
        self.fish_list.append(Fish(name, price_in_uah_per_kilo, origin))

    def get_fish_names_sorted_by_price(self):
        sorted_fish_list = sorted(self.fish_list, key=lambda x: x.price_in_uah_per_kilo)
        for i in sorted_fish_list:
            print("Fish name:", i.name, "\tprice:", i.price_in_uah_per_kilo)

    def sell_fish(self, fish_name: str, weight: float) -> float:
        self.weight = weight
        self.name = fish_name
        self.price_in_uah_per_kilo = 11.2
        return print(f'{self.name}: {self.price_in_uah_per_kilo * self.weight}')

    def cast_out_old_fish(self, name: str = "Unnamed fish",
                          price_in_uah_per_kilo: float = 100,
                          origin: str = "Unnamed country"):
        self.fish_list.remove(Fish(name, price_in_uah_per_kilo, origin))



class Seller:
    def sell_fish(self, name: str ='',
                  price_in_uah_per_kilo: float = 0):
        pass



class Buyer:
    def buy_fish(self, name: str = '',
                 price_in_uah_per_kilo: float = 0):
        pass


f = FishShop()
f.add_fish("goldFish", 120)
f.add_fish("salmon", 420)
f.add_fish("orange fish", 520)
f.get_fish_names_sorted_by_price()
f.sell_fish('salmon', 37.5)
