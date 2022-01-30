from datetime import datetime
import datetime


class Fish:
    age_in_month = 2
    weight = 3.6
    def __init(self):
        self.age_in_month = 2
        self.weight = 3.6

class fish_info(Fish):
    name = 'salmon'
    origin = 'Norway'
    price_in_uah_per_kilo = 15.5
    catch_date = datetime.time(0, 3)
    due_date = datetime.time(0, 7)
    is_alive = True
    def __init(self):
        self.name = 'salmon'
        self.origin = 'Norway'
        self.catch_date = datetime.time(0, 3)
        self.due_date = datetime.time(0, 7)
        self.is_alive = True

class fish_box(fish_info):
    weight = 3.6
    height = 3.5
    depth = 1.5
    def __init(self):
        self.weight = 3.6
        self.height = 3.5
        self.width = 1.5

class FishShop(fish_box):
    frozen_fish_boxes = {fish_info.name: [fish_box.weight, fish_box.height, fish_box.depth, fish_box.is_alive]}
    fresh_fish = {}
    def __init(self):
        self.name=fish_info.name
        self.fish_boxes = {fish_info.name: [fish_box.weight, fish_box.height, fish_box.depth, fish_box.is_alive]}
        self.fresh_fish = {}

    def add_fishBox(self, frozen_fish_boxes):
        self.fish_boxes = {fish_info.name: [fish_box.weight, fish_box.height, fish_box.depth, fish_box.is_alive]}
        print('fish` name, box` weight, height, depth and if the fish inside is alive: ', self.fish_boxes)

    def add_fish(self, name: str, weight: float, price: float):
        fresh_fish[name] = [weight, price]


    def get_fish_names_sorted_by_price(self):
        sorted_fish = sorted(fresh_fish.items(), key=lambda fresh_fish: fresh_fish[1][1])
        print(sorted_fish)

    def sell_fish(self, name: str, weight: float) -> float:
        self.weight = Fish.weight
        self.name = fish_info.name
        self.price_in_uah_per_kilo = 11.2
        return print(f'{self.name}: {self.price_in_uah_per_kilo * self.weight}')


    #def cast_out_old_fish(self, name: str = "Unnamed fish",
    #                      price_in_uah_per_kilo: float = 100,
    #                      origin: str = "Unnamed country"):
    #    self.fish_list.remove(Fish(name, price_in_uah_per_kilo, origin))



class Seller:
    def sell_fish(self, name: str ='',
                  price_in_uah_per_kilo: float = 0):
        pass



class Buyer:
    def buy_fish(self, name: str = '',
                 price_in_uah_per_kilo: float = 0):
        pass
fish_obj = Fish()
fishinfo_obj = fish_info()
fishbox_obj = fish_box()
f = FishShop()
fresh_fish = {}
frozen_fish_boxes = {fishinfo_obj.name: [fishbox_obj.weight, fishbox_obj.height, fishbox_obj.depth, fishbox_obj.is_alive]}
f.add_fishBox(frozen_fish_boxes)
f.add_fish('goldfish', 40.5, 13.2)
f.add_fish('karas newVersion', 160.5, 45.6)
f.add_fish('karas', 60.5, 15.6)
f.get_fish_names_sorted_by_price()
f.sell_fish('salmon', 56.6)